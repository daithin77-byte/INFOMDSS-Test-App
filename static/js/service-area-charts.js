// Renders charts for the service-area test dashboard using data supplied by
// the Flask backend (see modules/data.py) and injected into the page as
// operatorChartData / topInjectionChartData / topWithdrawalChartData /
// timelineChartData before this script runs.

Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

function renderBarChart(canvasId, data, label, yLabel) {
    const canvas = document.getElementById(canvasId);
    if (!canvas || !data) return;
    new Chart(canvas, {
        type: 'bar',
        data: {
            labels: data.labels,
            datasets: [{
                label: label,
                backgroundColor: 'rgba(2,117,216,1)',
                borderColor: 'rgba(2,117,216,1)',
                data: data.values,
            }],
        },
        options: {
            scales: {
                xAxes: [{ gridLines: { display: false } }],
                yAxes: [{
                    ticks: { min: 0 },
                    gridLines: { display: true },
                    scaleLabel: { display: !!yLabel, labelString: yLabel },
                }],
            },
            legend: { display: false },
        },
    });
}

window.addEventListener('DOMContentLoaded', () => {
    const operatorCanvas = document.getElementById('operatorChart');
    if (operatorCanvas && typeof operatorChartData !== 'undefined') {
        new Chart(operatorCanvas, {
            type: 'pie',
            data: {
                labels: operatorChartData.labels,
                datasets: [{
                    data: operatorChartData.values,
                    backgroundColor: operatorChartData.colors,
                }],
            },
        });
    }

    if (typeof topInjectionChartData !== 'undefined') {
        renderBarChart('topInjectionChart', topInjectionChartData, 'Required Injection Capacity (MW)', 'MW');
    }
    if (typeof topWithdrawalChartData !== 'undefined') {
        renderBarChart('topWithdrawalChart', topWithdrawalChartData, 'Required Withdrawal Capacity (MW)', 'MW');
    }
    if (typeof timelineChartData !== 'undefined') {
        renderBarChart('timelineChart', timelineChartData, 'Service Areas', 'Count');
    }
});
