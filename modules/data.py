"""Demo data for the dashboard, tables, and charts pages.
"""

import csv
import os

_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_CSV_PATH = os.path.join(_PROJECT_ROOT, 'data', 'employees.csv')


def _load_employees():
    with open(_CSV_PATH, newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        row['age'] = int(row['age'])
    return rows


EMPLOYEES = _load_employees()


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
