# Providence, RI — LVT model handoff notes

Status: data discovery done, notebook **not yet written**. Pick up at `/lvt-city` Step 2 (model-policy),
then write `cities/providence/model.ipynb` per `.claude/skills/build-notebook.md`.

## Policy answers (the `/lvt-city` upfront questions, already answered by the user)

1. Government body: city levy. Providence is the only property-taxing entity (no county government in RI; schools are
   city-funded), so this is the whole real-property tax. Tangible personal property (Class 4, $53.40) is not modeled.
2. Reform: **4:1 split-rate**, revenue-neutral.
3. Existing structure: **keep all classes**. Apply the split *within* each rate class, revenue-neutral per class
   (Rochester pattern), preserving owner/non-owner rates, exemptions and full exemptions.
4. Official revenue figure: look it up (see "Revenue validation" below).

## Environment needs

- Network hosts: `webgis.providenceri.gov`, `data.providenceri.gov`, `www.providenceri.gov`,
  `tigerweb.geo.census.gov`, `api.census.gov` (plus `municipalfinance.ri.gov` for the state rate table).
- `CENSUS_API_KEY` must be in the session env (or the repo's gitignored `.env`) for the equity charts.

## Data sources (both are the same vintage: assessment date Dec 31, 2024 → FY2026 bills)

| Source | URL | Notes |
|---|---|---|
| Parcels + CAMA values (geometry) | `https://webgis.providenceri.gov/server/rest/services/PVD_Radius_Parcels_FL/FeatureServer/0` | 44,365 polygons, `TaxRollYear`=2025. Has `AssessedValueLand`, `AssessedValueBuildings`, `AssessedValueTotal`, `MuniUseCode`/`MuniUseCodeDesc`, `NumUnits`, `Owner1`, `ParcAddress`, `PROPID`. Load with `get_feature_data_with_geometry(dataset_name='PVD_Radius_Parcels_FL', base_url='https://webgis.providenceri.gov/server/rest/services', layer_id=0, paginate=True)`. Same data as MapServer `Parcels/PVD_Parcel_Boundaries/MapServer/0` ("Parcels with CAMA") but don't use `get_mapserver_data_with_geometry` — it hardcodes EPSG:3435. |
| 2025 Property Tax Roll (bills) | Socrata `6ub4-iebe`: `https://data.providenceri.gov/resource/6ub4-iebe.csv?$limit=100000` | 44,372 rows. `total_assmt`, `total_exempt`, `total_taxes` (billed), `class`/`short_desc`, `levy_code_1` (rate class), `tax_map`. Dataset description says "billed FY2025" but the bills match FY2026 rates (e.g. 39 Pratt St: 933,500 × 8.40 = 7,841.40) — trust the bills. |

**Wrong endpoint warning:** `services2.arcgis.com/qvkbeam7Wirps6zC/.../parcel_file_current` (returned by web search as
"Providence parcels") is **Detroit** (BSEED, Principal Residence Exemption, 377,940 parcels). Do not use it.

Cached locally (gitignored) in `cities/providence/data/`: `parcels_cama.gpq`, `tax_roll_2025.csv`.

## Cleaning findings

- **Roll duplicates:** the Socrata export repeats accounts (same `p_id`, differing only in situs address/point
  columns). `drop_duplicates('p_id')` → 44,062 accounts, **$352,655,566** billed real-property tax.
- **Join key:** roll `tax_map` (e.g. `043-0586-0000`) = GIS `PROPID`. After dedupe, ~all accounts join; assessed
  totals match 100% on the joined rows. A few hundred roll accounts (before dedupe: 329, incl. some TSA/combo/apt)
  have no GIS polygon — drop them from the parcel model and report count and $.
- GIS rows with blank `PROPID` are ROW/water slivers with $0 values — drop.
- **Condo canary (Gate 5):** all 4,128 condo units (`MuniUseCode` 23 residential, 24 commercial) have
  `AssessedValueLand = 0` (all value booked as building). Units of a complex share one identical polygon
  (complex = `PROPID[:8]`, i.e. plat-lot; 650 complexes, median 3 units, max 504). Must impute condo land before
  modeling, or condos will show a false large tax cut. Keep unit-level rows (units in one complex are in different
  rate classes: OO01 vs NO01). Options: (a) St. Paul pattern — kNN/neighborhood median land share of nearby
  non-condo parcels applied to each unit; (b) complex lot area (EPSG:3438 ft) × local land $/sf from nearby
  non-condo parcels, allocated to units by assessed value, capped at a sane share. (b) better reflects density
  (towers get low land share). Document the choice.

## Tax structure (FY2026 levy ordinance + RI Div. of Municipal Finance FY2026 rate table)

Rates per $1,000 of assessed value (100% of market value), assessment date Dec 31, 2024:

| `levy_code_1` | Class | Rate | Accounts | Billed |
|---|---|---|---|---|
| OO01 | 1A owner-occupied (1 unit, incl. owner-occ condos) | 8.40 | 12,984 | $56.9M |
| OO2-5 | 1B owner-occupied 2–5 units | 7.55 | 7,156 | $30.4M |
| NO01 | 1A non-owner-occupied (incl. NOO condos, residential vacant land) | 14.60 | 8,529 | $38.8M |
| NOO2-5 | 1B non-owner-occupied 2–5 units | 14.00 | 6,922 | $59.0M |
| C610 | 1C 6–10 units | 26.00 | 377 | $9.3M |
| C11 | 1D 11+ units | 28.50 | 133 | $18.5M |
| C01 | 2A commercial/industrial, CI vacant land, commercial condo, and "combo" mixed-use | 29.20 | 4,693 | $112.6M |
| TSA | Tax stabilization agreements (RIGL 44-3-9), contractual taxes | — | ~140 | ~$17M |
| 8LAW | Low-income housing taxed at 8% of rent (RIGL 44-5-13.11) | — | ~640 | ~$14.9M |
| PRA, R01 | 4 odd accounts | — | 4 | ~$8K |
| E01 | Fully exempt | 0 | ~2,500 | 0 |

(Accounts/billed for the rate classes are after dedupe; TSA/8LAW/E01 approximate.)

- Rebuilding `net × statutory rate` matches billed tax within 0.002% for every class **except C01 (−3.8%)**:
  mixed-use "combo" parcels (`class` 04-05U / 04-610 / 04-11+) are billed at a blend (residential rate on the
  residential portion, commercial on the rest — ordinance Class 3). Plan: use **billed `total_taxes` as
  `current_tax`**, and solve each class's split on rate-normalized values (value × effective rate / class nominal
  rate) so blended parcels keep their blend. For uniform-rate classes this is an ordinary per-class split-rate.
- Partial exemptions (`total_exempt` < `total_assmt`: veterans, 65+, disabled — ordinance Sec. 5, capped $ savings)
  → apply to improvements first, then land (LVTShift convention).
- Hold TSA, 8LAW, PRA, R01 out of the reform (taxes set by contract/statute, not by value); exclude them and E01
  from the export/charts and report counts and $.
- Owner-occupancy comes straight from `levy_code_1` — no need to infer it.

## Revenue validation (Gate 1)

- Ground truth for the parcel model: deduped roll billed total **$352.66M** (real property only).
- Official levy (FY26 approved levy ordinance, real + tangible combined): not less than **$396,211,044**, not more
  than $419,878,051. Real-property-only figure still needed: the gap is roughly tangible personal property. Candidate
  sources: the FY2025 ACFR (`https://www.providenceri.gov/wp-content/uploads/2026/01/FY25-Signed-Final-Report-and-Financial-Statements.pdf`, property-tax
  levy note/statistical tables) or the city budget book's "current year real estate" revenue line.
- FY2027 (Dec 31, 2025 assessment) adopted ordinance exists (`.../2026/06/FY27-Adopted-Ordinance-Book-Web.pdf`) with
  the same rates, but no FY2027 roll is published on the open-data portal yet, so model FY2026.

## Notebook constants

```python
CITY_NAME = 'providence'
STATE_FIPS = '44'
COUNTY_FIPS = '007'          # Providence County
MODEL_TYPE = 'split_rate:4.0'
LAND_IMPROVEMENT_RATIO = 4.0
PARCEL_ID_COL = 'PROPID'
OWNER_NAME_COL = 'Owner1'
OWNER_ADDRESS_COL = 'ParcAddress'
PARCEL_URL_TEMPLATE = None   # Vision (gis.vgsi.com/providenceri) uses internal pids — verify a deep link before setting
```

For the export's single `land_millage`/`improvement_millage`, use the revenue-weighted average of the per-class
rates (Rochester precedent) and document it.

## Category mapping hints (`MuniUseCodeDesc` / roll `short_desc`)

Single Family → Single Family Residential; 2-5 Family → Small Multi-Family (2-4 units) (note: 2–5 here);
apt 6-10 / apt 11+ / Apartments → Large Multi-Family (5+ units); Residential Condo → Condominium;
Commercial Condo → Office / Commercial Condo; combo 5U/6-10/11+ / Combination → Mixed Use;
Commercial I/II → Commercial (split further by use code if available); Industrial → Industrial;
Residential Vacant / CI Vacant Land / Commercial Ind Vct → Vacant Land; Utility → Other Commercial;
Farm Forest → Agricultural. Then the $0-improvement → Vacant Land override.
