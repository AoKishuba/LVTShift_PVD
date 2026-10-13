"""Build cities/providence/parcel_map.html: the shareable Providence parcel map, with a checkbox that
switches between the main citywide model (model.ipynb) and the per-class variant (model_per_class.ipynb).

Each notebook writes its own single-model map under analysis/reports/. This script combines their two
map exports into the one committed map. Run it after executing both notebooks, from any directory:

    python3 cities/providence/build_comparison_map.py
"""
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from lvt.parcel_map import create_parcel_map

MAPS_DIR = REPO_ROOT / 'analysis' / 'maps'
REPORTS_DIR = REPO_ROOT / 'analysis' / 'reports'

# Writes {output_dir}/{city}/parcel_map.html = cities/providence/parcel_map.html
create_parcel_map(
    MAPS_DIR / 'providence.parquet',
    'providence',
    output_dir=str(REPO_ROOT / 'cities'),
    charts_dir=str(REPORTS_DIR / 'providence'),
    alternative={
        'source': MAPS_DIR / 'providence_per_class.parquet',
        'label': 'Keep separate tax classes',
        'note': 'Each of the seven rate classes keeps its own rates and its current revenue.',
        'primary_note': 'One land rate and one building rate for every parcel; the seven rate classes are removed.',
        'charts_dir': str(REPORTS_DIR / 'providence_per_class'),
    },
)
