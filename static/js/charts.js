// Renders the Chart.js charts using data supplied by the Flask backend
// (see data.py) and injected into the page as areaChartData / barChartData /
// pieChartData before this script runs.

Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

window.addEventListener('DOMContentLoaded', () => {
    const areaCanvas = document.getElementById('myAreaChart');
    if (areaCanvas && typeof areaChartData !== 'undefined') {
        new Chart(areaCanvas, {
            type: 'line',
            data: {
                labels: areaChartData.labels,
                datasets: [{
                    label: 'Sessions',
                    lineTension: 0.3,
                    backgroundColor: 'rgba(2,117,216,0.2)',
                    borderColor: 'rgba(2,117,216,1)',
                    pointRadius: 5,
                    pointBackgroundColor: 'rgba(2,117,216,1)',
                    pointBorderColor: 'rgba(255,255,255,0.8)',
                    pointHoverRadius: 5,
                    pointHoverBackgroundColor: 'rgba(2,117,216,1)',
                    pointHitRadius: 50,
                    pointBorderWidth: 2,
                    data: areaChartData.values,
                }],
            },
            options: {
                scales: {
                    xAxes: [{
                        time: { unit: 'date' },
                        gridLines: { display: false },
                        ticks: { maxTicksLimit: 7 },
                    }],
                    yAxes: [{
                        ticks: { min: 0, maxTicksLimit: 5 },
                        gridLines: { color: 'rgba(0, 0, 0, .125)' },
                    }],
                },
                legend: { display: false },
            },
        });
    }

    const barCanvas = document.getElementById('myBarChart');
    if (barCanvas && typeof barChartData !== 'undefined') {
        new Chart(barCanvas, {
            type: 'bar',
            data: {
                labels: barChartData.labels,
                datasets: [{
                    label: 'Revenue',
                    backgroundColor: 'rgba(2,117,216,1)',
                    borderColor: 'rgba(2,117,216,1)',
                    data: barChartData.values,
                }],
            },
            options: {
                scales: {
                    xAxes: [{
                        time: { unit: 'month' },
                        gridLines: { display: false },
                        ticks: { maxTicksLimit: 6 },
                    }],
                    yAxes: [{
                        ticks: { min: 0, maxTicksLimit: 5 },
                        gridLines: { display: true },
                    }],
                },
                legend: { display: false },
            },
        });
    }

    const pieCanvas = document.getElementById('myPieChart');
    if (pieCanvas && typeof pieChartData !== 'undefined') {
        new Chart(pieCanvas, {
            type: 'pie',
            data: {
                labels: pieChartData.labels,
                datasets: [{
                    data: pieChartData.values,
                    backgroundColor: pieChartData.colors,
                }],
            },
        });
    }
});
