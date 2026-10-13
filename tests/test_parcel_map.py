"""Tests for the parcel map (lvt.parcel_map): the ratio slider, shared-lot merging and the model checkbox."""
import json
import re
import sys
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
from shapely.geometry import box

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lvt.lvt_utils import model_split_rate_tax
from lvt.parcel_map import _parse_split_ratio, _ratio_slider_spec, create_parcel_map


def _parcels(rate=10.0):
    # vacant lot, building-heavy, mixed, land-heavy; current tax = flat rate on value
    df = pd.DataFrame({
        'taxable_land_value':        [100_000.0, 50_000.0, 200_000.0, 80_000.0],
        'taxable_improvement_value': [0.0, 250_000.0, 300_000.0, 20_000.0],
    })
    df['current_tax'] = (df['taxable_land_value'] + df['taxable_improvement_value']) * rate / 1000
    return df


def _split(df, ratio, **kwargs):
    _, _, _, out = model_split_rate_tax(
        df, 'taxable_land_value', 'taxable_improvement_value', df['current_tax'].sum(), ratio, **kwargs)
    return out


def _as_export(df, model_type='split_rate:4.0'):
    df = df.copy()
    df['model_type'] = model_type
    return gpd.GeoDataFrame(df, geometry=[box(i, 0, i + 1, 1) for i in range(len(df))], crs='EPSG:4326')


def _closed_form(spec, land, bldg, codes, ratio):
    # the formula the browser applies
    out = np.empty(len(land))
    for k, g in enumerate(spec['groups']):
        m = codes == k
        out[m] = g['T'] * (ratio * land[m] + bldg[m]) / (ratio * g['L'] + g['B'])
    return out


def test_parse_split_ratio():
    assert _parse_split_ratio('split_rate:4.0') == 4.0
    assert _parse_split_ratio('split_rate_10to1') == 10.0
    assert _parse_split_ratio('split_rate:4.0,exemption:50000') is None
    assert _parse_split_ratio('abatement_75pct') is None


def test_plain_split_rate_enables_slider_and_matches_other_ratios():
    spec = _ratio_slider_spec(_as_export(_split(_parcels(), 4.0)), 'testcity')
    assert spec is not None
    assert spec['ratio'] == 4.0 and spec['today'] is True
    assert [g['label'] for g in spec['groups']] == ['All modeled parcels']
    land, bldg, codes = spec['arrays']
    # re-solving in closed form at 2:1 must equal re-running the model at 2:1
    at_two = _split(_parcels(), 2.0)['new_tax'].to_numpy()
    assert np.allclose(_closed_form(spec, land, bldg, codes, 2.0), at_two)


def test_capped_model_disables_slider():
    df = _parcels()
    df['cap'] = 0.012  # tax capped at 1.2% of value binds on the vacant lot at 4:1
    capped = _split(df, 4.0, percentage_cap_col='cap')
    assert capped['tax_capped'].any()
    assert _ratio_slider_spec(_as_export(capped), 'testcity') is None


def test_per_group_basis_keeps_group_order_and_revenue():
    low, high = _parcels(rate=8.0), _parcels(rate=29.0)
    low['cls'], high['cls'] = 'Residential', 'Commercial'
    modeled = pd.concat([_split(low, 4.0), _split(high, 4.0)], ignore_index=True)
    modeled['ratio_basis_land'] = modeled['taxable_land_value']
    modeled['ratio_basis_improvement'] = modeled['taxable_improvement_value']
    modeled['ratio_group'] = pd.Categorical(modeled['cls'], categories=['Residential', 'Commercial'])
    spec = _ratio_slider_spec(_as_export(modeled), 'testcity')
    assert spec is not None
    assert [g['label'] for g in spec['groups']] == ['Residential', 'Commercial']
    land, bldg, codes = spec['arrays']
    land_only = _closed_form(spec, land, bldg, codes, 1e12)
    for k, g in enumerate(spec['groups']):
        assert np.isclose(land_only[codes == k].sum(), g['T'])   # each class keeps its revenue
    # treating the two classes as one group no longer reproduces the per-class model
    pooled = modeled.drop(columns=['ratio_group'])
    assert _ratio_slider_spec(_as_export(pooled), 'testcity') is None


def test_accounts_sharing_a_lot_polygon_are_drawn_once(tmp_path):
    # two condo units on one lot polygon, two separate lots
    export = _as_export(_split(_parcels(), 4.0))
    export['parcel_id'] = ['A-1', 'A-2', 'B', 'C']
    export = export.set_geometry([box(0, 0, 1, 1), box(0, 0, 1, 1), box(2, 0, 3, 1), box(4, 0, 5, 1)])
    out = create_parcel_map(export, 'testcity', output_dir=str(tmp_path), simplify_tolerance_m=None)
    html = Path(out).read_text()
    data = json.loads(re.search(r'const DATA = (.*?);\nconst CENTER', html, flags=re.S).group(1))
    lots = [f['properties'] for f in data['features']]
    assert len(lots) == 3
    shared = next(p for p in lots if 'u' in p)
    assert [a['pid'] for a in shared['u']] == ['A-1', 'A-2']
    units = export[export['parcel_id'].isin(['A-1', 'A-2'])]
    assert np.isclose(shared['cur'], units['current_tax'].sum())
    assert np.isclose(shared['new'], units['new_tax'].sum())
    assert np.isclose(shared['pct'], round((units['new_tax'].sum() / units['current_tax'].sum() - 1) * 100, 1))
    assert all('bl0' in a and 'g0' in a for a in shared['u'])   # each unit is re-solved by the ratio slider


def _two_models():
    primary = _as_export(_split(_parcels(), 4.0))
    alternative = _as_export(_split(_parcels(), 2.0), model_type='split_rate:2.0')
    for frame in (primary, alternative):
        frame['parcel_id'] = ['A', 'B', 'C', 'D']
    return primary, alternative.iloc[::-1].reset_index(drop=True)   # row order may differ between exports


def _map_payload(path):
    html = Path(path).read_text()
    models = json.loads(re.search(r'const MODELS = (.*?);\n', html).group(1))
    data = json.loads(re.search(r'const DATA = (.*?);\nconst CENTER', html, flags=re.S).group(1))
    return models, [f['properties'] for f in data['features']]


def test_alternative_model_is_lined_up_by_parcel_id(tmp_path):
    primary, alternative = _two_models()
    out = create_parcel_map(primary, 'testcity', output_dir=str(tmp_path), simplify_tolerance_m=None,
                            alternative={'source': alternative, 'label': 'Use 2:1'})
    models, accounts = _map_payload(out)
    assert [m['spec']['ratio'] for m in models] == [4.0, 2.0] and models[1]['label'] == 'Use 2:1'
    by_id = {a['pid']: a for a in accounts}
    for model, frame in enumerate([primary, alternative]):
        spec = models[model]['spec']
        g = spec['groups'][0]
        for _, row in frame.iterrows():
            a = by_id[row['parcel_id']]
            # the browser's closed form for this model reproduces that model's new_tax for the same account
            new = g['T'] * (spec['ratio'] * a[f'bl{model}'] + a[f'bi{model}']) / (spec['ratio'] * g['L'] + g['B'])
            assert np.isclose(new, row['new_tax'], atol=0.01)


def test_alternative_must_describe_the_same_bills(tmp_path):
    primary, alternative = _two_models()
    alternative.loc[0, 'parcel_id'] = 'Z'
    try:
        create_parcel_map(primary, 'testcity', output_dir=str(tmp_path), alternative={'source': alternative, 'label': 'x'})
    except ValueError as err:
        assert 'different parcel_ids' in str(err)
    else:
        raise AssertionError('mismatched accounts should be rejected')
