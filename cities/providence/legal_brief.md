# Providence, Rhode Island — LVT Legal Brief

**Date of analysis:** 2026-11-11 (first drafted 2026-10-19; every quoted statute, charter section and case holding re-checked against its source on 2026-11-11)
**Status (one line):** Not available by ordinance today, but no constitutional barrier was found. A land/building rate split needs one act of the General Assembly. Once that act passes, the City Council adopts the split by ordinance.
**Recommended vehicle:** A — direct split-rate (a land rate and a lower improvement rate). Enact it as a general local-option amendment to R.I. Gen. Laws chapter 44-5, which Providence then adopts by ordinance.
**Pathway tier:** 5 (general state enabling). The fallback is Tier 4, a Providence-only amendment to § 44-5-11.18. It is faster and matches how every recent Providence tax change was made, but after *Myles Standish Associates v. City of Providence* (R.I. July 29, 2026) a one-city act carries an open Article XIII § 4 local-vote risk. A referendum clause would cure that risk, making it Tier 6.
**Confidence:** Medium. The operative statutes were read verbatim on the General Assembly's statute server. The constitutional text comes from official bill reproductions and from search excerpts, because the constitution pages could not be reached from the research environment. The case law comes from the Division of Municipal Finance's official digest of one-line holdings, not from the full opinions. No Rhode Island decision addresses separate land and improvement rates, and *Myles Standish* was read only through its syllabus and press coverage.

**Scope and assumptions.** The brief covers the City of Providence real-property levy, which is the whole property tax on Providence real estate (Rhode Island has no county property tax, and the city funds its schools). It tests the two reforms modeled in this folder:
1. **Main model ([`model.ipynb`](model.ipynb)):** one citywide land rate and one building rate, revenue-neutral in total, with the seven rate classes removed (land 26.68, building 6.67 per $1,000).
2. **Per-class variant ([`model_per_class.ipynb`](model_per_class.ipynb)):** a 4:1 split solved inside each existing rate class, with each class keeping its current revenue.

The request set no scope, so these defaults were used: every legal pathway is evaluated, and the brief is action-ready (draft statutory language is in §9).

---

## 1. Jurisdictional snapshot

- **State / entity.** Providence is a city governed by the *Providence Home Rule Charter of 1980* ([Charter](https://council.providenceri.gov/wp-content/uploads/2022/03/Home-Rule-Charter-Editable-Version.pdf), Part I). Population was about 191,000 at the 2020 Census.
- **Home rule.** Rhode Island has constitutional home rule (R.I. Const. art. XIII), but home rule expressly excludes taxation (art. XIII, § 5, quoted in §2.4). **For property-tax purposes Providence works under a Dillon's-Rule-like regime: it has only the taxing powers the General Assembly grants.**
- **Taxing authorities on a Providence parcel.**
  - The City of Providence levy, which is the only general property tax and is the subject of this brief.
  - Since July 1, 2026, a **state** tax on non-owner-occupied residential property assessed above $1M ([R.I. Gen. Laws ch. 44-72](https://webserver.rilegislature.gov/Statutes/TITLE44/44-72/INDEX.htm)). It is administered by the Division of Taxation, its proceeds go to the low-income housing tax credit fund (§ 44-72-4(b)), and it is outside the city's control.
  - Special assessments of any district management authority formed under chapter 45-59.
- **Current levy.**
  - FY2026: "not less than … ($396,211,044)" on real and tangible property, at rates set in Code of Ordinances § 21-182 ([FY26 Approved Ordinance Book](https://www.providenceri.gov/wp-content/uploads/2025/07/FY26-Approved-Ordinance-Book.pdf), § 1, § 4).
  - FY2027: "a sum not less than … ($418,954,285) AND NOT MORE THAN … ($435,712,456)", with the same rates as FY2026 ([FY27 Adopted Ordinance Book](https://www.providenceri.gov/wp-content/uploads/2026/06/FY27-Adopted-Ordinance-Book-Web.pdf), § 1, § 4).
  - Rates per $1,000 (§ 21-182(c)): Class 1A non-owner 14.60 / owner-occupied 8.40; Class 1B non-owner 14.00 / owner-occupied 7.55; Class 1C (6–10 units) 26.00; Class 1D (11+ units) 28.50; Class 2A commercial/industrial 29.20; Class 3 mixed use billed at a residential/commercial blend; Class 4 tangible property 53.40.
- **Modeled base.** $321.6M of FY2026 real-property bills across 40,515 rate-class accounts. Held out of the model:
  - 133 tax-stabilization (TSA) accounts ($14.5M), taxed under § 44-3-9 agreements;
  - 638 low-income housing accounts ($12.4M), taxed on rent under § 44-5-13.11;
  - fully exempt property.

## 2. Constitutional layer (Layer 1)

### 2.1 Rhode Island has no property-tax uniformity clause; it has a general "fairly distributed" principle

The constitution has no section specific to property taxation. The constraint that functions as a uniformity requirement is in the Declaration of Rights:

> "All free governments are instituted for the protection, safety, and happiness of the people. All laws, therefore, should be made for the good of the whole; and the burdens of the state ought to be fairly distributed among its citizens. No person shall be deprived of life, liberty or property without due process of law, nor shall any person be denied equal protection of the laws."
> — R.I. Const. art. I, § 2 (current text as reproduced in [2024 S 2431](https://webserver.rilegislature.gov/BillText24/SenateText24/S2431.htm), a proposed amendment that quotes the section in full; [official page](https://www.rilegislature.gov/riconstitution/Constitution/C01.aspx))

**Layer-1 pattern:** closest to the *no uniformity clause* pattern (NY / IA / CT). The only constraint is a general fairness-and-equal-protection principle, which courts read as a reasonable-classification test. Rhode Island has none of the stricter patterns: no "uniform upon the same class" text (PA), no "in proportion to value" (TX), and no "all real estate one class" (WA).

### 2.2 Judicial interpretation: reasonable classification is permitted; uniformity is required within a class

From the Division of Municipal Finance's official digest, [*Rhode Island Local Taxation Supreme Court Cases — Chronological Listing*](https://municipalfinance.ri.gov/documents/resources/lawschrono.pdf) (holdings quoted as digested; full opinions not reviewed):

- ***Manufacturers' Mutual Fire Ins. Co. v. Clarke*, 41 R.I. 277 (1918):** "While burden of taxation should be distributed fairly among citizens, absolute fairness and equality is unattainable. Legislature may classify persons and property for tax purposes and impose different burdens upon different classes, provided such classification is not unreasonable or arbitrary."
- ***Allen v. Bonded Municipal Corp.*, 62 R.I. 101 (1938):** "Constitutional requirement of fairness met if a taxing law demands that it be applied with substantial uniformity, without discrimination throughout a class of property set apart for separate taxation."
- ***Rosen v. Restrepo*, 119 R.I. 398 (1977):** if the assessor "is assessing at less than 100 percent of value he must comply with constitutional directive that burdens of state be fairly distributed among its citizens and apply same percentage factor to each piece of property."
- ***McTwiggan v. Hunter*, 18 R.I. 776 (1895):** "The whole assessment is illegal, due to lack of uniform distribution, when the assessors intentionally omit property liable to taxation …"
- ***Brown University v. Granger*, 19 R.I. 704 (1897):** "Constitutional provision stating that 'burdens of state ought to be fairly distributed among its citizens' does not affect property exempted from taxation by charter of university."
- ***Woonsocket Hospital v. Quinn*, 54 R.I. 424 (1934):** "Laws exempting property from taxation must be strictly construed …"

**Reading.**
- *Clarke* and *Allen* together give the operative rule: the legislature may set property apart in classes with different burdens if the classification is not arbitrary, and each class must be taxed uniformly within itself.
- Separating land from improvements, with a stated economic purpose (taxing location value that owners did not create, and not penalizing construction), is a classification with an articulable rational basis. Each component class would be taxed at one rate citywide, or one rate per existing use class, which satisfies *Allen*.
- **No Rhode Island case addresses a land/improvement differential directly**, so openness at Layer 1 is strongly indicated but not confirmed.
- *Rosen* matters for design. It constitutionalizes the same-percentage rule for assessment ratios, so the split should be built through **rates** on full-value assessments, not through different assessment ratios for land and buildings (see §10).

**Federal overlay.** Under the Fourteenth Amendment, property-tax classifications get rational-basis review: [*Nordlinger v. Hahn*, 505 U.S. 1 (1992)](https://supreme.justia.com/cases/federal/us/505/1/). [*Allegheny Pittsburgh Coal Co. v. County Comm'n*, 488 U.S. 336 (1989)](https://supreme.justia.com/cases/federal/us/488/336/) bars only intentional, systematic unequal assessment *within* a class. A legislated, uniformly applied land/improvement split clears both.

### 2.3 Classification and exemption authority

- **No express grant is needed and none exists.** The General Assembly's taxing and exemption power is plenary unless the constitution limits it. The former residual-powers clause (art. VI, § 10, "The general assembly shall continue to exercise the powers it has heretofore exercised, unless prohibited in this Constitution") was removed by the separation-of-powers amendments approved by voters in 2004 (per [PolitiFact's account](https://politifact.com/factchecks/2014/jan/19/nicholas-gorham/former-ri-rep-nicholas-gorham-says-state-general-a/); confirm the date), so this brief does not rely on it. The legislature's authority over local taxation is confirmed by art. XIII, § 5 (below).
- **Exemptions are statutory** (e.g., [§ 44-3-3](https://webserver.rilegislature.gov/Statutes/TITLE44/44-3/44-3-3.htm)) and strictly construed (*Woonsocket Hospital*). A city cannot create a general building exemption on its own.

### 2.4 Home rule — the provisions that decide who must act

- **Art. XIII, § 2** (local legislative powers): "Every city and town shall have the power at any time to adopt a charter, amend its charter, enact and amend local laws relating to its property, affairs and government not inconsistent with this Constitution and laws enacted by the general assembly in conformity with the powers reserved to the general assembly." (Current text as reproduced in [2012 H 7713](https://webserver.rilegislature.gov/BillText12/HouseText12/H7713.htm).)
- **Art. XIII, § 5** (local taxing and borrowing powers): "Nothing contained in this article shall be deemed to grant to any city or town the power to levy, assess and collect taxes or to borrow money, except as authorized by the general assembly." (Text as reproduced by [Justia, art. XIII](https://law.justia.com/constitution/rhode-island/C13.html); confirm against the [official page](https://www.rilegislature.gov/riconstitution/Constitution/C13.aspx).)
- **Art. XIII, § 4** (powers of the general assembly over cities and towns): "The general assembly shall have the power to act in relation to the property, affairs and government of any city or town by general laws which shall apply alike to all cities and towns, but which shall not affect the form of government of any city or town." The section continues that the general assembly "shall also have the power to act in relation to the property, affairs and government of a particular city or town provided that such legislative action shall become effective only upon approval" by a majority of that city's or town's qualified electors. (Verbatim to that point; the remainder, which concerns tax and spending acts in *towns*, should be confirmed on the official page.)

**The 2026 development.** In [*Myles Standish Associates, LP v. City of Providence*, No. 2025-223-Appeal (R.I. July 29, 2026)](https://www.courts.ri.gov/Opinions/Supreme-25-223.pdf) ([Justia summary](https://law.justia.com/cases/rhode-island/supreme-court/2026/25-223.html)), the Supreme Court held:
- A General Assembly act that let Providence's Board of Licenses exempt one address from a liquor-license restriction related to the "affairs" of the city.
- It was "void under article 13, section 4" for lack of local voter approval.
- The Superior Court had treated liquor licensing as a statewide concern needing no local vote. The Supreme Court vacated that judgment and remanded for entry of judgment for the challenger.

[Press coverage](https://rhodeislandcurrent.com/2026/08/17/liquor-license-ruling-raises-questions-about-general-assemblys-role-in-special-exemptions/) reported that legislative attorneys are reviewing other single-municipality "notwithstanding" acts. As of November 11, 2026, no legislative response (bill, joint resolution or change in special-act practice) was found.

**Why this matters here.** Every recent Providence tax change was a one-city act passed without a local vote: § 44-5-11.18 (P.L. 2024, chs. 115/116; P.L. 2025, chs. 348/349), the FY2026 levy-cap waiver (§ 44-5-2(h)), and the 2000 Downcity tax district (P.L. 2000, ch. 449). There is a strong argument that § 5 takes special *tax* acts out of § 4:
- § 5 reserves taxing power to the General Assembly.
- Taxation has historically been treated as a state concern under the *Town of East Greenwich v. O'Neil*, 617 A.2d 104 (R.I. 1992) test.

That argument is untested after *Myles Standish*. A Providence-only LVT act should therefore be drafted either as a general law (no § 4 issue) or with its own local-approval clause.

### 2.5 Constitutional caps

None. The Rhode Island Constitution contains no property-tax rate cap, no levy-growth cap, no assessment-ratio rule, and no acquisition-value lock. All limits are statutory (§5 below). Because no constitutional cap exists, there is no voted-levy carve-out to find.

## 3. Statutory layer (Layer 2)

### 3.1 The general classification statute classifies by use and closes the list of classes

[R.I. Gen. Laws § 44-5-11.8](https://webserver.rilegislature.gov/Statutes/TITLE44/44-5/44-5-11.8.htm):

> "(a) Upon the completion of any comprehensive revaluation or any update, in accordance with § 44-5-11.6, any city or town may adopt a tax classification plan, by ordinance, with the following limitations:
> (1) The designated classes of property shall be limited to the classes as defined in subsection (b) of this section."

The subsection (b) classes are defined by use and property type:
- Class 1: "Residential real estate consisting of no more than five (5) dwelling units; land classified as open space; and dwellings on leased land including mobile homes";
- Class 2: "Commercial and industrial real estate; residential properties containing partial commercial or business uses; and residential real estate of more than five (5) dwelling units";
- Class 3: tangible personal property;
- Class 4: motor vehicles.

The general 50% rate-differential limit (§ 44-5-11.8(a)(2)) and the same-percentage-change rule ((a)(3)) apply "except in the city of Providence."

Subsection (l): "The city council of the city of Providence may, by ordinance, provide for, and adopt, a tax rate on various classes as they shall deem appropriate. Provided, that the provisions of § 44-5-11.18(4) shall apply."

### 3.2 Providence's own classification statute: "unrestricted tax rates," but only across use classes

[R.I. Gen. Laws § 44-5-11.18](https://webserver.rilegislature.gov/Statutes/TITLE44/44-5/44-5-11.18.htm) (enacted P.L. 2024, chs. 115/116; amended P.L. 2025, chs. 348/349):

> "Notwithstanding any provision of § 44-5-11.8 to the contrary, the city of Providence may adopt a tax classification with unrestricted tax rates by ordinance as follows: (1) Classes of property. (i)(A) Class 1A: Residential real estate consisting of one dwelling unit. … (D) Class 1 D: Residential real estate of more than ten (10) dwelling units. (ii)(A) Class 2A: Commercial I real estate, as defined by the Providence tax assessor on an annual basis. (B) Class 2B: Commercial II real estate, as defined by the Providence tax assessor on an annual basis. (iii) Class 3: Properties containing partial residential and commercial or business uses. … (iv) Class 4: All ratable, tangible personal property."

> "(4) The tax rate for Class 2A shall not be more than two (2) times the base tax rate of Class 1A; and the tax rate for Class 2A shall not be more than three and one-half (3½) times the effective owner-occupied tax rate of Class 1A, whether by homestead exemption or separate rates. The tax rate for Class 2B shall not be more than one and one-half (1.5) times the tax rate for Class 2A. There shall be no further differential tax rate limits for a tax classification adopted pursuant to this section."

**Chain:**
1. Every Providence class is a class of "real estate" defined by use and unit count, with no class for land or for improvements.
2. § 44-5-11.8(a)(1) limits classes to those enumerated.
3. Therefore neither statute authorizes a separate rate on land and on buildings, and **Vehicle A is blocked at Layer 2 (statute), not Layer 1.**

The city's own ordinance confirms this reading. Its classes are "pursuant to R.I.G.L. 44-5-11.18," and its Class 3 apportionment is by use, not by land vs. building (§ 21-182(b)).

**Design trap for the per-class variant.** The § 44-5-11.18(4) ratio caps are written against a single "tax rate" per class. The per-class model's solved rates would breach them if the caps were read against land rates or building rates separately:
- Class 2A land 52.31 vs. Class 1A non-owner land 24.78 is 2.11×, above the 2× cap;
- Class 2A land 52.31 vs. owner-occupied land 14.37 is 3.64×, above the 3½× cap.

Each class's *effective* rate (total tax ÷ total value) is unchanged in that model, so the caps hold on an effective-rate reading. Enabling language must say which rate the caps apply to (see §9 draft, (a)(3)). The citywide model uses one rate pair for every class and satisfies the caps trivially.

### 3.3 Assessment statute: one value, one uniform ratio

[R.I. Gen. Laws § 44-5-12(a)](https://webserver.rilegislature.gov/Statutes/TITLE44/44-5/44-5-12.htm):

> "All real property subject to taxation shall be assessed at its full and fair cash value, as of December 31 in the year of the last revaluation, statistical revaluation or update thereto, or at a uniform percentage thereof, not to exceed one hundred percent (100%), with such value to be determined by the assessors in each town or city."

This, with *Rosen v. Restrepo*, blocks a "back-door split" through different assessment ratios for land and buildings.

### 3.4 Existing improvement-only exemptions and stabilizations: proof of concept, but narrow

- **Tax stabilization / exemption for new or rehabilitated property.** [§ 44-3-9(a)(1)](https://webserver.rilegislature.gov/Statutes/TITLE44/44-3/44-3-9.htm) lets the city council, "for a period not exceeding twenty (20) years, … exempt from payment, in whole or in part, real and personal property which has undergone environmental remediation, is historically preserved, or is used for affordable housing, manufacturing, commercial, or residential purposes, or to determine a stabilized amount of taxes," after public hearings and findings that the exemption "will inure to the benefit of the city or town." Findings may rest on the "willingness of a manufacturing or commercial or residential firm or property owner to construct new or to replace, reconstruct, convert, expand, retain, or remodel existing buildings" (§ 44-3-9(a)(1)(ii)).
  - § 44-3-9(b): "Cities shall have the same authority as is granted to towns except that authority granted to the qualified electors of a town and to town councils shall be exercised in the case of a city by the city council."
  - § 44-3-9(e): exempted property still pays the portion of the tax that services city debt.
- **Development property.** [§ 44-5-12(a)(6)](https://webserver.rilegislature.gov/Statutes/TITLE44/44-5/44-5-12.htm), statewide, exempts unsold new construction on development property from tax on improvements for up to two tax years. It says expressly: "the exemptions set forth in this section shall not apply to land." This is an existing **building-only exemption** in Rhode Island law.
- **Municipality-specific improvement exemptions.**
  - Pawtucket, [§ 44-5-13.2.5](https://webserver.rilegislature.gov/Statutes/TITLE44/44-5/44-5-13.2.5.htm): "an exemption from real property taxation equal to any increase in assessed valuation not exceeding fifteen thousand dollars ($15,000) cumulatively resulting from alterations and improvements";
  - Warwick and Central Falls, § 44-5-12(a)(3)–(4): improvements exempt from reassessment until the next revaluation.
- **Providence precedent.** [P.L. 2000, ch. 449](https://webserver.rilegislature.gov/PublicLaws00/law00449.htm) let the council create a Downcity Tax District where "eligible properties shall pay annual taxes on land and buildings in an amount equal to the tax assessed as of December 31, 1998 … regardless of increased property value resulting from substantial rehabilitation." It was a ten-year freeze on improvement-driven value increases. Successors are [§ 44-3-31.2](https://webserver.rilegislature.gov/Statutes/TITLE44/44-3/44-3-31.2.htm) and [§ 44-3-31.3](https://webserver.rilegislature.gov/Statutes/TITLE44/44-3/44-3-31.3.htm) (landmark mills and the arts district).

These show that the General Assembly regularly grants improvement-only relief, often to one municipality. None of them is a general, permanent building exemption or a land/improvement rate split.

### 3.5 Carve-outs for and against Providence

- **For.** Providence is the most favored municipality in the classification statutes:
  - exempt from the 50% differential and the same-percentage-change rules (§ 44-5-11.8(a)(2)–(3));
  - may adopt classification "with unrestricted tax rates" (§ 44-5-11.18). Its "notwithstanding" clause reads as freeing Providence from § 44-5-11.8's revaluation-year trigger;
  - may redefine unit thresholds by ordinance (§ 44-5-11.18(3)).
- **Against.** The ratio caps in § 44-5-11.18(4) are the only differential limits. Property taxed under TSAs (§ 44-3-9) or the 8% low-income housing law ([§ 44-5-13.11](https://webserver.rilegislature.gov/Statutes/TITLE44/44-5/44-5-13.11.htm), "a tax that equals eight percent (8%) of the property's previous years' gross scheduled rental income") is outside any value-based rate and is unaffected by a split.

### 3.6 Pending legislation

- **No Rhode Island bill for a land value tax, split-rate, or universal building exemption was found** in searches of the General Assembly's bill-text server and LegiScan-indexed sources for 2022–2026 (re-checked November 11, 2026). The 2027 session opens in January, so bills for it have not yet been introduced.
- The most recent Providence classification bill, [2025 H 6394](https://webserver.rilegislature.gov/BillText25/HouseText25/H6394.htm), was introduced at the request of the "City of Providence." Its explanation reads: "This act would adopt a new tax classification system for the city of Providence." It amended §§ 44-5-2, 44-5-11.8, 44-5-11.18 and 44-5-12, which is the template a split-rate bill would follow.
- [2025 H 6162](https://webserver.rilegislature.gov/BillText25/HouseText25/H6162.htm) (Providence levy-cap waiver) followed the same route.
- One-town classification acts remain routine. [2026 S 2577](https://webserver.rilegislature.gov/Billtext/BillText26/SenateText26/S2577.pdf), referred to Senate Housing & Municipal Government, "would enable the town of Portsmouth to adopt, repeal, or modify their tax classification plan for any tax year on and after December 31, 2026."

## 4. Local authority (Layer 3)

- **Taxing power under the charter is derivative.** Charter § 401: "The legislative powers of the city shall be vested in a city council, which shall have and exercise all powers vested in it by this Charter and by the laws of the state. The powers and duties of the city council shall include … (c) To adopt the annual city budget appropriation ordinance and levy taxes." The power to levy is exercised under state law (art. XIII, § 5), and the rate structure lives in Code § 21-182 (classification) and § 21-126 (exemptions), both amended each year in the levy ordinance.
- **Procedure.**
  - Charter § 410(b): "No ordinance shall be passed until it has been read on two (2) separate occasions at least forty-eight (48) hours elapsing between the first and the second readings."
  - § 411(d): a public hearing on 10 days' published notice is required before final action on "New taxes or increases in the rate of existing taxes." A split-rate raises the land rate.
  - § 412: mayoral veto; "if after such reconsideration two-thirds of the entire city council shall vote in favor of passage thereof, it shall become effective notwithstanding the mayor's action."
- **No citizen-initiated route.** Charter § 209: the initiative "shall not extend to the budget or capital programs or to any ordinance relating to the appropriation of money, or to the levy of taxes." Providence has no financial town meeting.
- **Prior history.**
  - Classification: under § 44-5-11.8 (enacted 2000, with Providence-specific exceptions), and since 2024 under its own § 44-5-11.18. Owner-occupied homes in Classes 1A and 1B currently get a separate lower rate (§ 21-182(c)(1)–(2)).
  - Improvement-value relief: the Downcity Tax District (2000), landmark/mill programs (2002, 2010), and routine TSAs.
  - No LVT or split-rate proposal by the city or its legislative delegation was found.

## 5. Caps, limits, circuit breakers (Layer 4)

- **Levy growth cap (statutory, total levy only).** [§ 44-5-2(b)](https://webserver.rilegislature.gov/Statutes/TITLE44/44-5/44-5-2.htm): "In its fiscal year 2013 and in each fiscal year thereafter, a city or town may levy a tax in an amount not more than four percent (4%) in excess of the total amount levied and certified by that city or town for its previous fiscal year."
  - Exceptions (§ 44-5-2(d)): lost non-property revenue, certified emergency, debt service, major new-construction growth, and Providence-specific FY2026 items in (d)(5) and (h). Any excess "shall be approved by the affirmative vote of at least four-fifths (⅘) of the full membership of the governing body" (§ 44-5-2(e)).
  - **Effect on LVT: none if the shift is revenue-neutral.** The cap limits the size of the levy, not how it is apportioned. Both modeled reforms hold the total constant.
- **No rate cap, no assessment-growth cap, no acquisition-value lock.** § 44-5-11.6(a)(1)(iii) cuts the other way: "Cities and towns shall not change the assessment of any property based on the purchase price of the property after a transfer occurs except in accordance with a townwide or citywide revaluation or update schedule." That is an anti-"welcome stranger" rule, consistent with a uniform market-value base.
- **No bill-level circuit breaker.** Rhode Island's Property Tax Relief Act ([ch. 44-33](https://webserver.rilegislature.gov/Statutes/TITLE44/44-33/INDEX.htm)) pays eligible households a state-funded "income tax credit or rebate from state funds" (§ 44-33-5). It does not cap or refund the city bill, so a split-rate's shift is not neutralized the way Indiana's caps neutralize South Bend's.
- **Voted levies.** No voter-approved excess-levy mechanism exists for Rhode Island cities. The cap override is a council supermajority, not a referendum (§ 44-5-2(e)).
- **Instruments outside the cap.**
  - District management authority assessments: "will not be considered to be a tax of the municipality for purposes of § 44-5-2" ([§ 45-59-15](https://webserver.rilegislature.gov/Statutes/TITLE45/45-59/45-59-15.htm)).
  - Tax-increment amounts pledged to TIF bonds, "for a period not to exceed twenty-five (25) years" ([§ 45-33.2-21(b)](https://webserver.rilegislature.gov/Statutes/TITLE45/45-33.2/45-33.2-21.htm)).

## 6. Assessment foundation (Layer 5)

- **Full market value, separately stated land and improvements.**
  - § 44-5-12(a) requires full and fair cash value, and Providence assesses at 100%.
  - The Department of Revenue's rules for updates must include "(2) A rebuilding of land value tables; (3) A rebuilding of cost tables of all improvement items; and (4) A rebuilding of depreciation schedules" ([§ 44-5-11.6(b)](https://webserver.rilegislature.gov/Statutes/TITLE44/44-5/44-5-11.6.htm)). That is, land and improvements are valued separately by rule.
  - Parcel-level `AssessedValueLand` and `AssessedValueBuildings` are public in the city's "Parcels with CAMA" GIS layer, and the model uses them directly.
- **Cycle.** "each city and town shall conduct a revaluation within nine (9) years of the date of the prior revaluation and shall conduct an update of real property every three (3) years from the last revaluation" (§ 44-5-11.6(a)(1)(ii)).
  - The current values are as of **December 31, 2024**, the city's 2024 revaluation by Vision Government Solutions ([ABC6 report](https://www.abc6.com/?p=3662077)), which first appeared on FY2026 bills.
  - The next update is due as of December 31, 2027, for FY2029 bills.
  - Between updates, values are frozen: "There shall be no adjustment to an assessment because of an increase or decrease in such value as a result of market forces in years when there is no revaluation …" (§ 44-5-12(a)).
- **Special regimes that bypass value-based rates.**
  - Farm, forest and open-space use-value: "the assessors shall consider no factors in determining the full and fair cash value of the real estate other than those that relate to that use" (§ 44-5-12(a)(2); ch. 44-27).
  - The 8% rent-based low-income housing tax (§ 44-5-13.11).
  - TSAs (§ 44-3-9).
  - Renewable-energy real property at "three dollars and fifty cents ($3.50) per kilowatt" of capacity (§ 44-5-12(a)(5)).
  - Development-property improvement exemption (§ 44-5-12(a)(6)).
  - These are small in Providence. The model holds TSA and 8%-law accounts at today's tax.
- **Condominium land — a real foundation defect, fixable by statute or assessor practice.**
  - The Condominium Act requires that "each unit must be separately taxed and assessed" ([§ 34-36.1-1.05(b)](https://webserver.rilegislature.gov/Statutes/TITLE34/34-36.1/34-36.1-1.05.htm)).
  - Providence's roll books every condo unit with **$0 land**: the full unit value is carried as building. That is harmless under one rate, but under a split-rate it would hand condos a false building-rate discount.
  - The model imputes $0.45B of land to 4,299 accounts. Enabling legislation should direct the assessor to apportion each condominium's land to its units, for example by the unit's allocated interest in the common elements.
- **No acquisition-value or assessment-lock rule.** This is not a California or Michigan foundation problem.

## 7. Vehicles open / blocked / unlock-able

| Vehicle | Status | Primary block (if any) | Action to unlock |
|---|---|---|---|
| **A. Direct split-rate** | **Unlock-able** | Layer 2. § 44-5-11.8(a)(1) "classes … limited to the classes as defined" (use classes of "real estate"); § 44-5-11.18 defines only use classes; § 44-5-12(a) single full-value assessment. No Layer-1 block: art. I, § 2 permits reasonable classification (*Clarke* 1918; *Allen* 1938) | General local-option statute (Tier 5), or a Providence amendment to § 44-5-11.18 (Tier 4; Tier 6 if it carries a referendum clause to remove the art. XIII, § 4 risk); then council ordinance |
| **B. Universal building exemption** | **Unlock-able** | Exemptions are statutory and strictly construed (*Woonsocket Hospital v. Quinn*, 54 R.I. 424 (1934)); the city has no power to create one (art. XIII, § 5) | General Assembly enactment of a local-option 100% improvement exemption (Tier 4/5). Building-only exemptions already exist in narrower form (§ 44-5-12(a)(6); § 44-5-13.2.5) |
| **C. Partial improvement exemption / abatement** | **Partially open; fully unlock-able** | A citywide fractional improvement exemption needs statute (same as B). Open today only for new or rehabilitated property via § 44-3-9, case by case, after hearings and findings, for at most 20 years, with the debt-service share still payable (§ 44-3-9(e)) | Today: an ordinance and program of § 44-3-9 abatements on added improvement value (Tier 1). Citywide: statute (Tier 4/5) |
| **D. Classification shift within existing classes** | **Open** | None. § 44-5-11.18 gives Providence "unrestricted tax rates" across use classes, within the (4) ratio caps | Council ordinance amending § 21-182 (Tier 1). Note: the council can also *narrow or remove* the class differentials by ordinance. That is the class-removal half of the main model, and it is legal today |
| **E. Voted-levy LVT** | **Blocked / not needed** | No voter-approved excess-levy mechanism for cities; the cap override is a ⅘ council vote (§ 44-5-2(e)); charter § 209 bars initiatives on "the levy of taxes." Nothing caps rates, so there is nothing for a voted levy to escape | None recommended |
| **F. Tax-increment / value capture** | **Open (value capture only)** | Cannot carry a differential land rate: "Nothing in this subsection allows for unequal apportionment or assessment of the taxes … an owner of real property within the tax increment district shall pay real property taxes apportioned equally with property taxes paid elsewhere in the city or town" (§ 45-33.2-27(b)(3)) | Council creates a district and master plan under §§ 45-33.2-23, -26 (Tier 1). Useful as a complement, not as LVT |
| **G. Special assessment district** | **Open (narrow), reading unverified** | Chapter 45-59 district management authorities. Petition by owners of "sixty percent (60%) of the aggregate assessed valuation of all real property" (§ 45-59-5(a)); "more than fifty percent (50%) of area of the land … devoted to commercial and retail uses" ((a)(6)); assessments capped at 10% of district property taxes (§ 45-59-16); purposes limited to district services (§ 45-59-9). Basis may be "(i) assessed valuation … (ii) square footage of land or improvements … (v) formulas establishing different assessment levels for different classes of real property, or (vi) any other method which reasonably apportions the expenses" (§ 45-59-5(a)(7)) | Owner petition plus council ordinance (§ 45-59-4) for a land-value-based district assessment (Tier 1, owner-initiated). Providence (pop. > 100,000) qualifies (§ 45-59-3(a)(5)). Confirm that "assessed valuation" may mean land valuation alone |
| **H. Transitional abatement on a flat rate** | **Unlock-able** (partial precedent) | Same as B/C for a citywide phase-in. P.L. 2000, ch. 449 (Downcity) is a precedent for a one-city improvement-value freeze | Statute authorizing a scheduled, declining improvement abatement (Tier 4/5), or a phase-in clause inside the Vehicle A statute (see §9 draft) |

A and C are legally equivalent in posture here: both need one statute, and neither faces a constitutional bar. The choice between them is practical (see §9).

## 8. Pathway tier scoring

| Tier | Pathway | Vehicle(s) at this tier |
|---|---|---|
| 1 | Ordinance alone | D (rate classes, including removing them); C, new or rehabilitated property only, via § 44-3-9; F (TIF, value capture only); G (district management authority with a land-based assessment, after a 60%-of-value owner petition) |
| 2 | Ordinance + local referendum | None. No local referendum route for tax ordinances (charter § 209; no financial town meeting) |
| 3 | Opt-in to existing state statute | None. No existing split-rate or building-exemption option to opt into |
| 4 | State enabling legislation (city-specific) | A, B, C, H. Amend § 44-5-11.18; this is the established route for Providence tax structure. **Risk:** art. XIII, § 4 after *Myles Standish* (2026) |
| 5 | State enabling legislation (general) | **A (recommended)**, B, C, H. A local-option section any city or town may adopt by ordinance; "general laws which shall apply alike to all cities and towns" need no local vote (art. XIII, § 4) |
| 6 | State enabling + local referendum | A, B, C, H. The Tier 4 bill with a Providence approval clause, which removes the § 4 question at the cost of an election |
| 7 | State constitutional amendment | Not required. No constitutional barrier identified |
| 8 | Amendment + assessment overhaul | Not applicable. Full-value assessment with three-year updates |

**Closest worked example.** **Syracuse, NY** (guide §7.4). Both states lack a property-tax uniformity clause, both bind cities by statute, and both offer a use-based option today (NY's homestead option; Providence's § 44-5-11.18). Rhode Island is **more permissive** than New York in practice:
- its General Assembly enacts municipality-specific tax structure almost every session;
- Providence already holds the state's broadest classification grant ("unrestricted tax rates").

The new art. XIII, § 4 question is the one way Rhode Island is *less* straightforward.

## 9. Recommended pathway and legal chain of thought

### 9.1 The chain

1. **Constitution permits it.** Art. I, § 2 requires that "the burdens of the state ought to be fairly distributed," and the Supreme Court reads that to let the legislature "classify persons and property for tax purposes and impose different burdens upon different classes, provided such classification is not unreasonable or arbitrary" (*Clarke*, 1918). A land class and an improvement class, each taxed uniformly, meets that standard and the within-class rule of *Allen* (1938). The federal rational-basis test is satisfied as well (*Nordlinger*). → **No amendment needed.**
2. **But the city cannot act alone.** Art. XIII, § 5 withholds from cities "the power to levy, assess and collect taxes … except as authorized by the general assembly." The only classification authority Providence holds (§§ 44-5-11.8, 44-5-11.18) is limited to use classes of "real estate," and § 44-5-12(a) requires one full-value assessment at a uniform percentage. → **One statute is required.**
3. **The statute should be a general local-option law.** Art. XIII, § 4 lets the General Assembly legislate for cities "by general laws which shall apply alike to all cities and towns" with no local vote, while an act for "a particular city or town" takes effect "only upon approval" of its voters. After *Myles Standish* (2026), whether a Providence-only tax act needs that approval is unsettled. A general opt-in statute avoids the question entirely, and it is more durable against repeal. → **Tier 5.**
4. **Providence then adopts by ordinance.** Under the new section and its existing levy power (Charter § 401(c)), the council sets a land rate and an improvement rate in § 21-182:
   - two readings (Charter § 410(b));
   - a public hearing, because the land rate rises (§ 411(d));
   - mayoral approval or a ⅔ override (§ 412).
5. **Nothing in Layer 4 interferes.** The § 44-5-2 cap governs the total levy, and both modeled reforms are revenue-neutral. There is no rate cap and no circuit breaker that would refund the shift. → **The modeled shift is the actual shift.**
6. **Economic outcome.** The levy is apportioned on land at N× the improvement rate. In the citywide model that means land 26.68 and buildings 6.67 per $1,000 at 4:1. In the per-class model it means a 4:1 pair inside each of the seven classes, with each class's revenue unchanged.

### 9.2 Draft statutory language (Tier 5 general local option)

> **§ 44-5-11.19. Land and improvement tax rates — Local option.**
> (a) Notwithstanding §§ 44-5-11.8 and 44-5-11.18, or any other general or special law to the contrary, the city or town council of any city or town may, by ordinance, provide that the tax on ratable real property, or on any class of real property adopted under § 44-5-11.8 or § 44-5-11.18, shall be levied at one rate upon the assessed value of land and at a lower rate upon the assessed value of buildings and other improvements, subject to the following:
> (1) Within each class, the rate on land shall be uniform, the rate on improvements shall be uniform, and the rate on improvements shall not exceed the rate on land;
> (2) The assessor shall state separately the full and fair cash value of the land and of the improvements of every parcel assessed under § 44-5-12. For each condominium, the value of the land shall be apportioned among the units in proportion to each unit's allocated interest in the common elements;
> (3) For purposes of §§ 44-5-11.8(a)(2) and 44-5-11.18(4), the tax rate of a class shall be its effective rate, equal to the total tax levied on the class divided by the total assessed value of the class;
> (4) The ordinance may phase in the ratio of the land rate to the improvement rate in equal annual steps over a period not exceeding ten (10) years, and may be adopted in any tax year, whether or not a revaluation or update is implemented in that year.
> (b) Nothing in this section authorizes any city or town to exceed the maximum levy under § 44-5-2.
> (c) Property taxed under an agreement pursuant to § 44-3-9, under § 44-5-13.11, or under chapter 27 of this title shall continue to be taxed as provided therein.
> (d) Exemptions of assessed value granted under chapter 3 of this title shall be applied first to the assessed value of improvements and then to the assessed value of land.

Notes on the draft:
- **(a)** allows both modeled structures: one citywide pair (the main model) or a pair within each existing class (the per-class model).
- **(a)(3)** prevents the ratio-cap trap described in §3.2.
- **(a)(4)** builds in Vehicle H (phase-in) and decouples adoption from the revaluation trigger in § 44-5-11.8(a).
- **(c)** matches the model's treatment of TSA, 8%-law and use-value property.
- **(d)** matches the model's exemption convention.

**Tier 4 fallback.** Add a new subsection (5) to § 44-5-11.18 containing the operative text of (a)(1)–(4) and (d), limited to Providence. To remove the art. XIII, § 4 question, add: "This act shall take effect upon approval by a majority of the qualified electors of the city of Providence voting thereon at a general or special election" (Tier 6).

### 9.3 Sequence of actions

1. **2027 session (January–June):** introduce the § 44-5-11.19 bill, ideally preceded by a City Council resolution requesting it (the H 6394 route). Municipal tax bills have gone to House Municipal Government & Housing (2025 H 6394) and Senate Housing & Municipal Government (2026 S 2577). A simple majority in each chamber plus the Governor's signature is needed.
2. **Council ordinance amending § 21-182** to set land and improvement rates (two readings, public hearing, mayor). Earliest practical bills: FY2028 if the act passes before the June 2027 levy ordinance; more likely FY2029, which coincides with the December 31, 2027 statistical update.
3. **Assessor:** apportion land to condo units before the first split-rate roll (the draft's (a)(2)). The model shows this moves $0.45B of value from building to land.
4. **Optional:** begin at 2:1 and step to 4:1 under (a)(4).

### 9.4 Which reform to adopt is a separate choice from the legal path

- **Class removal (the main model's first step) is already legal by ordinance** (Vehicle D, Tier 1). Setting every class to one rate satisfies § 44-5-11.18(4) trivially. It is also the largest and most contentious part of the main model: it shifts about $68M a year onto owner-occupied homes (owner-occupied single-family median +70%) before any land/building split. That outcome is a policy decision, not a legal constraint.
- **The per-class variant isolates the land/building split.** It keeps every class's revenue, so it leaves the § 44-5-11.18 structure and the owner-occupied rate intact. The same statute ((a), "any class") authorizes it. Politically, it is the smaller ask.

### 9.5 Fallbacks, in order

1. **Tier 4 (Providence amendment to § 44-5-11.18),** with a referendum clause if the session's lawyers read *Myles Standish* to reach tax acts.
2. **Vehicle C as a statute (local-option fractional improvement exemption, e.g., 75%).** It produces the same economics as 4:1, but it shrinks the taxable base. That may change state-aid formulas keyed to assessed value (see §11), which is why it ranks below A.
3. **Vehicle C under existing § 44-3-9, today:** a council program abating tax on *added* improvement value for new construction and substantial rehabilitation, for up to 20 years. It is narrow, but it can start now.
4. **Vehicle G:** a land-value-based district management authority assessment in a commercial district. It is small (≤10% of district taxes) and owner-initiated, but it is the only land-only levy available without new law.

### 9.6 Reversibility

A general local-option statute is harder to repeal than a one-city carve-out: repeal would take away an option other municipalities may be using. Compare Amsterdam, NY (authorized 1993, repealed) and Altoona, PA (adopted 2011, reverted 2016). This is a second reason to prefer Tier 5. At the local level, the council can repeal or change the ratio in any levy ordinance. The phase-in clause gives a natural review point at each step.

## 10. Creative pathways considered

| Idea | Outcome | Defeating (or supporting) text |
|---|---|---|
| Read § 44-5-11.18's "unrestricted tax rates" and the assessor-defined Class 2A/2B ("Commercial I/II real estate, as defined by the Providence tax assessor on an annual basis") as room for land and improvement classes | **Rejected** | Every class is a class of "real estate" by use; § 44-5-11.8(a)(1): classes "shall be limited to the classes as defined." Assessor definitions can sort parcels, not split one parcel's value |
| Assess land at 100% and buildings at a lower ratio | **Rejected** | § 44-5-12(a): "at a uniform percentage thereof"; *Rosen v. Restrepo* (1977): "apply same percentage factor to each piece of property" |
| Use § 44-3-9 as a citywide building abatement | **Partly viable** | Requires public hearings and findings tied to new or expanded investment; at most 20 years; debt-service share still payable (§ 44-3-9(e)). Works for new or rehabilitated buildings only |
| Use a TIF district as a land-rate overlay | **Rejected** | § 45-33.2-27(b)(3): no "unequal apportionment or assessment"; taxes "apportioned equally with property taxes paid elsewhere" |
| District management authority assessment on land value | **Viable, narrow** | § 45-59-5(a)(7)(i)–(vi) lets the petition choose the basis; capped by § 45-59-16 |
| Voted excess levy on land | **Not available, not needed** | No voted-levy regime; no rate cap to escape |
| "Privilege" excise measured by land value, modeled on ch. 44-72 (a tax "upon the privilege of utilizing property as non-owner occupied residential property," § 44-72-4) | **Possible but unnecessary** | Still needs General Assembly authority (art. XIII, § 5), and there is no constitutional obstacle to the plain property-tax route. A state-level land surcharge of this kind is a separate, statewide policy, not a city LVT |
| Constitutional amendment | **Not needed** | No Layer-1 barrier |

## 11. Open questions and required follow-up research

1. **Read the full *Myles Standish* opinion and concurrence** ([courts.ri.gov](https://www.courts.ri.gov/Opinions/Supreme-25-223.pdf)). Does the court's reading of "affairs" in art. XIII, § 4 reach single-municipality *tax* acts, given § 5's reservation of taxing power? Did it retain, narrow, or discard the state-concern test of *Town of East Greenwich v. O'Neil*? This decides whether Tier 4 is safe without a referendum. Also watch the 2027 session for any General Assembly response to the decision.
2. **Confirm the art. XIII, §§ 4–5 text** on the official constitution page (it was unreachable from the research environment; text here is from official bill reproductions and search excerpts).
3. **Pull the full opinions** in *Manufacturers' Mutual v. Clarke* (1918), *Allen v. Bonded Municipal Corp.* (1938) and *Rosen v. Restrepo* (1977). The digest gives one-line holdings only. Also search for any Rhode Island decision on taxing land and improvements differently, or on the homestead / owner-occupied differentials.
4. **State aid interaction.** Determine whether a split-rate (values unchanged) and a building exemption (taxable base reduced) are treated differently by aid formulas keyed to assessed or equalized value. Candidates: education aid's equalized weighted assessed valuation, distressed-community aid (§ 45-13-12), and PILOT aid (§ 45-13-5.1). This is the main practical tiebreaker between Vehicles A and B/C.
5. **Assessor practice.** Confirm with the Providence Assessor how condo land is valued and whether units can carry apportioned land under the CAMA system. Confirm that December 31, 2024 was a full revaluation and when the next statistical update falls.
6. **Vehicle G reading.** Ask the City Solicitor whether "assessed valuation" in § 45-59-5(a)(7)(i) may be limited to land valuation, or whether that requires (vi) "any other method which reasonably apportions."
7. **Who to consult.**
   - Division of Municipal Finance / Office of Municipal Affairs (Department of Revenue), which administers chapter 35 disclosure and the levy cap;
   - Providence City Solicitor and Council legal staff;
   - Rhode Island League of Cities and Towns (home rule practice after *Myles Standish*);
   - Rhode Island Assessors' Association;
   - Legislative Council drafting attorneys;
   - Lincoln Institute of Land Policy, for comparative split-rate statutes (PA Title 11; VA § 58.1-3221.1).

## 12. Sources

**Primary — constitution and courts**
- [R.I. Const. art. I (official)](https://www.rilegislature.gov/riconstitution/Constitution/C01.aspx); text of § 2 as quoted in [2024 S 2431](https://webserver.rilegislature.gov/BillText24/SenateText24/S2431.htm)
- [R.I. Const. art. XIII (official)](https://www.rilegislature.gov/riconstitution/Constitution/C13.aspx); [Justia art. XIII](https://law.justia.com/constitution/rhode-island/C13.html); text of § 2 as quoted in [2012 H 7713](https://webserver.rilegislature.gov/BillText12/HouseText12/H7713.htm)
- [*Myles Standish Associates, LP v. City of Providence*, No. 2025-223-Appeal (R.I. July 29, 2026)](https://www.courts.ri.gov/Opinions/Supreme-25-223.pdf); [Justia summary](https://law.justia.com/cases/rhode-island/supreme-court/2026/25-223.html)
- [R.I. Division of Municipal Finance — Rhode Island Local Taxation Supreme Court Cases, Chronological Listing](https://municipalfinance.ri.gov/documents/resources/lawschrono.pdf) (*McTwiggan v. Hunter*; *Brown University v. Granger*; *Manufacturers' Mutual Fire Ins. Co. v. Clarke*; *Woonsocket Hospital v. Quinn*; *Allen v. Bonded Municipal Corp.*; *Rosen v. Restrepo*)
- *Town of East Greenwich v. O'Neil*, 617 A.2d 104 (R.I. 1992)
- [*Nordlinger v. Hahn*, 505 U.S. 1 (1992)](https://supreme.justia.com/cases/federal/us/505/1/); [*Allegheny Pittsburgh Coal Co. v. County Comm'n*, 488 U.S. 336 (1989)](https://supreme.justia.com/cases/federal/us/488/336/)

**Primary — statutes, session laws and bills**
- [§ 44-5-2 Maximum levy](https://webserver.rilegislature.gov/Statutes/TITLE44/44-5/44-5-2.htm)
- [§ 44-5-11.6 Assessment of valuations — revaluation and updates](https://webserver.rilegislature.gov/Statutes/TITLE44/44-5/44-5-11.6.htm)
- [§ 44-5-11.8 Tax classification](https://webserver.rilegislature.gov/Statutes/TITLE44/44-5/44-5-11.8.htm)
- [§ 44-5-11.18 Tax classification — Providence](https://webserver.rilegislature.gov/Statutes/TITLE44/44-5/44-5-11.18.htm)
- [§ 44-5-12 Assessment at full and fair cash value](https://webserver.rilegislature.gov/Statutes/TITLE44/44-5/44-5-12.htm)
- [§ 44-5-13.2.5 Pawtucket — residential improvements exemption](https://webserver.rilegislature.gov/Statutes/TITLE44/44-5/44-5-13.2.5.htm)
- [§ 44-5-13.11 Low-income housing — 8% of rent](https://webserver.rilegislature.gov/Statutes/TITLE44/44-5/44-5-13.11.htm)
- [§ 44-3-3 Property exempt](https://webserver.rilegislature.gov/Statutes/TITLE44/44-3/44-3-3.htm); [§ 44-3-9 Exemption or stabilizing of taxes](https://webserver.rilegislature.gov/Statutes/TITLE44/44-3/44-3-9.htm); [§ 44-3-31.2](https://webserver.rilegislature.gov/Statutes/TITLE44/44-3/44-3-31.2.htm); [§ 44-3-31.3](https://webserver.rilegislature.gov/Statutes/TITLE44/44-3/44-3-31.3.htm)
- [Ch. 44-33 Property Tax Relief](https://webserver.rilegislature.gov/Statutes/TITLE44/44-33/INDEX.htm)
- [Ch. 44-72 Non-Owner Occupied Property Tax Act](https://webserver.rilegislature.gov/Statutes/TITLE44/44-72/INDEX.htm) ([§ 44-72-4](https://webserver.rilegislature.gov/Statutes/TITLE44/44-72/44-72-4.htm), [§ 44-72-6](https://webserver.rilegislature.gov/Statutes/TITLE44/44-72/44-72-6.htm))
- [Ch. 45-33.2 Municipal Tax Increment Financing Act](https://webserver.rilegislature.gov/Statutes/TITLE45/45-33.2/INDEX.htm) ([§ 45-33.2-21](https://webserver.rilegislature.gov/Statutes/TITLE45/45-33.2/45-33.2-21.htm), [§ 45-33.2-23](https://webserver.rilegislature.gov/Statutes/TITLE45/45-33.2/45-33.2-23.htm), [§ 45-33.2-27](https://webserver.rilegislature.gov/Statutes/TITLE45/45-33.2/45-33.2-27.htm))
- [Ch. 45-59 District Management Authorities](https://webserver.rilegislature.gov/Statutes/TITLE45/45-59/INDEX.htm) ([§ 45-59-3](https://webserver.rilegislature.gov/Statutes/TITLE45/45-59/45-59-3.htm), [§ 45-59-4](https://webserver.rilegislature.gov/Statutes/TITLE45/45-59/45-59-4.htm), [§ 45-59-5](https://webserver.rilegislature.gov/Statutes/TITLE45/45-59/45-59-5.htm), [§ 45-59-9](https://webserver.rilegislature.gov/Statutes/TITLE45/45-59/45-59-9.htm), [§ 45-59-15](https://webserver.rilegislature.gov/Statutes/TITLE45/45-59/45-59-15.htm), [§ 45-59-16](https://webserver.rilegislature.gov/Statutes/TITLE45/45-59/45-59-16.htm))
- [§ 34-36.1-1.05 Condominiums — separate titles and taxation](https://webserver.rilegislature.gov/Statutes/TITLE34/34-36.1/34-36.1-1.05.htm)
- [P.L. 2000, ch. 449 — Downcity section of Providence](https://webserver.rilegislature.gov/PublicLaws00/law00449.htm)
- [2025 H 6394 — Providence tax classification](https://webserver.rilegislature.gov/BillText25/HouseText25/H6394.htm); [2025 H 6162 — Providence levy cap](https://webserver.rilegislature.gov/BillText25/HouseText25/H6162.htm); [2026 S 2577 — Portsmouth tax classification](https://webserver.rilegislature.gov/Billtext/BillText26/SenateText26/S2577.pdf)

**Primary — City of Providence**
- [Providence Home Rule Charter of 1980](https://council.providenceri.gov/wp-content/uploads/2022/03/Home-Rule-Charter-Editable-Version.pdf) (§§ 209, 401, 410, 411, 412)
- [FY2026 Approved Ordinance Book](https://www.providenceri.gov/wp-content/uploads/2025/07/FY26-Approved-Ordinance-Book.pdf) (levy ordinance; Code §§ 21-182, 21-126)
- [FY2027 Adopted Ordinance Book](https://www.providenceri.gov/wp-content/uploads/2026/06/FY27-Adopted-Ordinance-Book-Web.pdf)
- Models: [`model.ipynb`](model.ipynb) and [`model_per_class.ipynb`](model_per_class.ipynb) in this folder

**Secondary (context only, not load-bearing)**
- [Rhode Island Current — "Liquor license ruling raises questions about General Assembly's role in special exemptions" (Aug. 17, 2026)](https://rhodeislandcurrent.com/2026/08/17/liquor-license-ruling-raises-questions-about-general-assemblys-role-in-special-exemptions/)
- [ABC6 — "Providence launches 2024 revaluation program"](https://www.abc6.com/?p=3662077)
- [Rhode Island Current — Providence levy-cap negotiations (2025)](https://rhodeislandcurrent.com/2025/06/26/providence-city-council-leaders-and-smiley-agree-to-seek-5-85-tax-levy-hike/)
- [Pierce Atwood — New Rhode Island tax on non-owner-occupied properties](https://www.pierceatwood.com/alerts/new-rhode-island-tax-non-owner-occupied-properties-assessed-1-million-or-more)

*Research tool, not legal advice. Before drafting legislation or advising the council, re-verify every authority above with a Rhode Island–admitted attorney. That applies especially to the art. XIII, § 4 question, which turns on a decision less than four months old.*
