document.addEventListener("DOMContentLoaded", function () {
    // 各グラフを作成
    const ctxTemp = document.getElementById("temperatureChart").getContext("2d");
    new Chart(ctxTemp, {
        type: "line",
        data: {
            labels: timestamps, // HTMLから埋め込まれたデータ
            datasets: [{
                label: "温度 (°C)",
                data: temperatureData,
                borderColor: "rgba(255, 99, 132, 1)",
                backgroundColor: "rgba(255, 99, 132, 0.2)",
                fill: true,
            }],
        },
        options: {
            responsive: true,
            scales: {
                x: { title: { display: true, text: "時刻" } },
                y: { title: { display: true, text: "温度 (°C)" } },
            },
        },
    });

    const ctxSoil = document.getElementById("soilMoistureChart").getContext("2d");
    new Chart(ctxSoil, {
        type: "line",
        data: {
            labels: timestamps,
            datasets: [{
                label: "土壌水分 (%)",
                data: soilMoistureData,
                borderColor: "rgba(54, 162, 235, 1)",
                backgroundColor: "rgba(54, 162, 235, 0.2)",
                fill: true,
            }],
        },
        options: {
            responsive: true,
            scales: {
                x: { title: { display: true, text: "時刻" } },
                y: { title: { display: true, text: "土壌水分 (%)" } },
            },
        },
    });

    const ctxGas = document.getElementById("gasResistanceChart").getContext("2d");
    new Chart(ctxGas, {
        type: "line",
        data: {
            labels: timestamps,
            datasets: [{
                label: "ガス抵抗 (kΩ)",
                data: gasResistanceData,
                borderColor: "rgba(75, 192, 192, 1)",
                backgroundColor: "rgba(75, 192, 192, 0.2)",
                fill: true,
            }],
        },
        options: {
            responsive: true,
            scales: {
                x: { title: { display: true, text: "時刻" } },
                y: { title: { display: true, text: "ガス抵抗 (kΩ)" } },
            },
        },
    });
});
