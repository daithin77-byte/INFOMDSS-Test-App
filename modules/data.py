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


def _parse_mw(value):
    """'78.5 MW' -> 78.5; '-' or '' -> None."""
    if not value:
        return None
    match = re.match(r'^\s*(-?\d+(?:\.\d+)?)', value)
    return float(match.group(1)) if match else None


_PALETTE = [
    '#007bff', '#dc3545', '#ffc107', '#28a745',
    '#17a2b8', '#6610f2', '#fd7e14', '#20c997', '#6c757d',
]


def operator_counts():
    """Number of service areas each grid operator (rnb) appears in."""
    counts = {}
    for row in SERVICE_AREAS:
        for operator in row['rnb'].split(','):
            operator = operator.strip()
            if operator:
                counts[operator] = counts.get(operator, 0) + 1
    ordered = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
    labels = [k for k, _ in ordered]
    values = [v for _, v in ordered]
    colors = [_PALETTE[i % len(_PALETTE)] for i in range(len(labels))]
    return {'labels': labels, 'values': values, 'colors': colors}


def top_required_capacity(direction='Injection', limit=10):
    """The `limit` service areas with the highest required transport capacity."""
    field = f'requiredTransportCapacity{direction}'
    parsed = [(row['name'], _parse_mw(row[field])) for row in SERVICE_AREAS]
    parsed = [(name, mw) for name, mw in parsed if mw is not None]
    parsed.sort(key=lambda pair: pair[1], reverse=True)
    top = parsed[:limit]
    return {'labels': [name for name, _ in top], 'values': [mw for _, mw in top]}


def resolution_timeline(direction='Injection'):
    """Count of service areas by the year their congestion is expected to be solved."""
    field = f'yearSolved{direction}'
    counts = {}
    for row in SERVICE_AREAS:
        year = row[field].strip()
        label = year if year and year != '-' else 'Not scheduled'
        counts[label] = counts.get(label, 0) + 1
    # 'Not scheduled' sorts before any year string, since '' < '2026' etc.
    ordered = sorted(counts.items(), key=lambda kv: '' if kv[0] == 'Not scheduled' else kv[0])
    return {'labels': [k for k, _ in ordered], 'values': [v for _, v in ordered]}

