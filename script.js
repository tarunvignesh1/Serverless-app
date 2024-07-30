document.addEventListener('DOMContentLoaded', async function() {
    const form = document.getElementById('workout-form');
    form.addEventListener('submit', async function(event) {
        event.preventDefault();
        
        const username = document.getElementById('username').value;
        const workoutDay = document.getElementById('workout-day').value;
        const hours = document.getElementById('hours').value;
        const workoutDate = document.getElementById('workout-date').value;

        const data = {
            username,
            workoutDay,
            hours,
            workoutDate
        };

        try {
            const response = await fetch('https://your-api-gateway-endpoint.amazonaws.com/your-resource', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });

            if (response.ok) {
                alert('Workout logged successfully!');
                loadChartData(); // Refresh the chart data after logging the workout
            } else {
                alert('Error logging workout. Please try again.');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error connecting to server. Please try again.');
        }
    });

    async function loadChartData() {
        try {
            const response = await fetch('https://your-api-gateway-endpoint.amazonaws.com/your-get-resource', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                }
            });

            if (response.ok) {
                const data = await response.json();
                const chartData = formatChartData(data);
                renderChart(chartData);
            } else {
                alert('Error fetching chart data.');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error connecting to server.');
        }
    }

    function formatChartData(data) {
        const labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
        const chartData = Array(7).fill(0);

        data.forEach(entry => {
            const dayIndex = labels.indexOf(entry.workoutDay);
            if (dayIndex !== -1) {
                chartData[dayIndex] += entry.hours;
            }
        });

        return {
            labels,
            datasets: [{
                label: 'Hours Worked Out',
                data: chartData,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        };
    }

    function renderChart(chartData) {
        const ctx = document.getElementById('workout-chart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: chartData,
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    loadChartData(); // Load initial chart data
});
