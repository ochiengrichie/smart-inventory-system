// static/js/dashboard.js

document.addEventListener("DOMContentLoaded", function () {
    const chartElement = document.getElementById("inventoryChart");

    // Prevent error if chart not present
    if (!chartElement) return;

    const months = JSON.parse(chartElement.dataset.months);
    const counts = JSON.parse(chartElement.dataset.counts);

    new Chart(chartElement, {
        type: "bar",
        data: {
            labels: months,
            datasets: [
                {
                    label: "Items Added",
                    data: counts,
                    backgroundColor: "rgba(54, 162, 235, 0.7)",
                    borderRadius: 6,
                },
            ],
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: { stepSize: 10 },
                },
            },
            plugins: {
                legend: { display: false },
            },
        },
    });
});
