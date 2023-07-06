const getOptionChart = async () => {
    try {
        const response = await fetch("http://192.168.1.13:8000/get_chart/");
        return await response.json();
    } catch (ex) {
        alert(ex);
    }
};

const initChart = async () => {
    const myChart = echarts.init(document.getElementById("chart"));

    myChart.setOption(await getOptionChart());

    myChart.resize();
};


window.addEventListener("load", async () => {
    await initChart();
});