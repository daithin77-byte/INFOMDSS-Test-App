"""Demo data for the dashboard, tables, and charts pages.
"""

import csv
import os
import re

_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_CSV_PATH = os.path.join(_PROJECT_ROOT, 'data', 'nl_energy_service_areas.csv')
_EXCLUDED_COLUMNS = {'projects', 'history'}


def _humanize(column: str) -> str:
    """'existingTransportCapacityInjection' -> 'Existing Transport Capacity Injection'."""
    spaced = re.sub(r'(?<!^)(?=[A-Z])', ' ', column).replace('_', ' ')
    return spaced.strip().title()


def _load_service_areas():
    with open(_CSV_PATH, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        columns = [c for c in reader.fieldnames if c not in _EXCLUDED_COLUMNS]
        rows = [{c: row[c] for c in columns} for row in reader]
    return columns, rows


SERVICE_AREA_COLUMNS, SERVICE_AREAS = _load_service_areas()
SERVICE_AREA_COLUMN_LABELS = {c: _humanize(c) for c in SERVICE_AREA_COLUMNS}


def area_chart_data():
    return {
        'labels': ['Mar 1', 'Mar 2', 'Mar 3', 'Mar 4', 'Mar 5', 'Mar 6', 'Mar 7',
                   'Mar 8', 'Mar 9', 'Mar 10', 'Mar 11', 'Mar 12', 'Mar 13'],
        'values': [10000, 30162, 26263, 18394, 18287, 28682, 31274, 33259,
                   25849, 24159, 32651, 31984, 38451],
    }


def bar_chart_data():
    return {
        'labels': ['January', 'February', 'March', 'April', 'May', 'June'],
        'values': [4215, 5312, 6251, 7841, 9821, 14984],
    }


def pie_chart_data():
    return {
        'labels': ['Blue', 'Red', 'Yellow', 'Green'],
        'values': [12.21, 15.58, 11.25, 8.32],
        'colors': ['#007bff', '#dc3545', '#ffc107', '#28a745'],
    }
