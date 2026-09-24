# INFOMDSS Test App

Basic Flask dashboard to serve as a template for the INFOMDSS group project. Based on the [SB Admin Bootstrap](https://startbootstrap.com/template/sb-admin) template.


## Pages

- `/` – dashboard with Chart.js charts of Dutch grid service areas
- `/data` – full service-area data table

## Structure

```
app.py                              Flask routes
modules/data.py                     Loads CSV data, aggregates chart data
data/nl_energy_service_areas.csv    Service-area data
templates/                          Jinja2 templates (base.html + pages)
static/                             CSS, JS, images
```

See [DATA_SOURCES.md](DATA_SOURCES.md) for data details.
