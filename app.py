import os

from flask import Flask, abort, render_template
from modules.data import (
    SERVICE_AREA_COLUMN_LABELS,
    SERVICE_AREA_COLUMNS,
    SERVICE_AREAS,
    area_chart_data,
    bar_chart_data,
    pie_chart_data,
)

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")


# Primary App Routes ------------------------------------------------------------------------------
@app.route("/")
def dashboard():
    return render_template(
        "dashboard.html",
        service_areas=SERVICE_AREAS,
        columns=SERVICE_AREA_COLUMNS,
        column_labels=SERVICE_AREA_COLUMN_LABELS,
        area_chart=area_chart_data(),
        bar_chart=bar_chart_data(),
    )

@app.route("/charts")
def charts():
    return render_template(
        "charts.html",
        area_chart=area_chart_data(),
        bar_chart=bar_chart_data(),
        pie_chart=pie_chart_data(),
    )

@app.route("/tables")
def tables():
    return render_template(
        "tables.html",
        service_areas=SERVICE_AREAS,
        columns=SERVICE_AREA_COLUMNS,
        column_labels=SERVICE_AREA_COLUMN_LABELS,
    )

@app.route("/errors/<int:code>")
def demo_error(code):
    """Sidebar demo links that trigger a real Flask error response."""
    if code not in (401, 404, 500):
        abort(404)
    abort(code)


# Error Handlers ----------------------------------------------------------------------------------
@app.errorhandler(401)
def unauthorized(_error):
    return render_template("errors/401.html"), 401

@app.errorhandler(404)
def not_found(_error):
    return render_template("errors/404.html"), 404

@app.errorhandler(500)
def server_error(_error):
    return render_template("errors/500.html"), 500


if __name__ == "__main__":
    app.run(debug=False)
