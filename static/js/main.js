
const chart1 = echarts.init(document.querySelector('#main'));

console.log(chart1);

$(document).ready(() => {
    drawPM25()
}
)

function drawPM25() {
    $.ajax(
        {
            url: '/pm25-data',
            type: 'POST',
            dataType: 'json',

            success: (data) => {
                var option = {
                    title: {
                        text: 'PM2.5'
                    },
                    tooltip: {},
                    legend: {
                        data: ['鄉鎮']
                    },
                    xAxis: {
                        data: data['site']
                    },
                    yAxis: {},
                    series: [
                        {
                            name: 'PM2.5',
                            type: 'bar',
                            data: data['pm25']
                        }
                    ]
                };

                // 使用刚指定的配置项和数据显示图表。
                chart1.setOption(option);

                console.log(data);
            },
            error: () => {
                alert("讀取失敗")
            }
        }
    );
}

