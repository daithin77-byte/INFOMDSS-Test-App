import os

from flask import Flask, abort, flash, redirect, render_template, request, session, url_for
from modules.data import EMPLOYEES, area_chart_data, bar_chart_data, pie_chart_data

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")


@app.route("/")
def dashboard():
    return render_template(
        "dashboard.html",
        employees=EMPLOYEES,
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
    return render_template("tables.html", employees=EMPLOYEES)


@app.route("/errors/<int:code>")
def demo_error(code):
    """Sidebar demo links that trigger a real Flask error response."""
    if code not in (401, 404, 500):
        abort(404)
    abort(code)


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
