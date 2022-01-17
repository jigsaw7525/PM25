const chart1 = echarts.init(document.querySelector('#main'));
const chart2 = echarts.init(document.querySelector('#six'));
const chart3 = echarts.init(document.querySelector('#county'));

//自動縮放
window.onresize = function () {
    chart1.resize();
    chart2.resize();
    chart3.resize();
};

//jquery寫法
$('#county_btn').click(() => {
    const county = $('#select_county').val();
    drawCountyPM25(county);
})

$(document).ready(() => {
    drawPM25();
    drawSixPM25();
    drawCountyPM25("新北市");
});


function drawCountyPM25(county) {
    $.ajax(
        {
            url: `/county-pm25/${county}`,
            type: 'post',
            dataType: 'json',
            success: (data) => {
                console.log(data);
                // 指定图表的配置项和数据
                const option = {
                    title: {
                        text: county + '各區域PM2.5資訊'
                    },
                    tooltip: {},
                    legend: {
                        data: ['PM2.5']
                    },
                    xAxis: {
                        data: data['county']
                    },
                    yAxis: {},
                    series: [
                        {
                            showBackground: true,
                            itemStyle: {
                                // Styles for normal state.
                                normal: {
                                    color: '#00ff7f'
                                },
                                // Styles for emphasis state.
                                emphasis: {
                                    color: '#00ff7f'
                                }
                            },
                            name: 'pm2.5',
                            type: 'bar',
                            data: data['pm25']
                        }
                    ]
                };

                chart3.setOption(option);


            },
            error: () => alert('讀取失敗!'),
        }
    )
}


function drawSixPM25() {
    $.ajax(
        {
            url: '/six-data',
            type: 'post',
            dataType: 'json',
            success: (data) => {
                console.log(data);
                // 指定图表的配置项和数据
                const option = {
                    title: {
                        text: '六都平均PM2.5資訊'
                    },
                    tooltip: {},
                    legend: {
                        data: ['PM2.5']
                    },
                    xAxis: {
                        data: data['county']
                    },
                    yAxis: {},
                    series: [
                        {
                            showBackground: true,
                            itemStyle: {
                                // Styles for normal state.
                                normal: {
                                    color: '#661058'
                                },
                                // Styles for emphasis state.
                                emphasis: {
                                    color: '#981883'
                                }
                            },
                            name: 'pm2.5',
                            type: 'bar',
                            data: data['pm25']
                        }
                    ]
                };

                chart2.setOption(option);


            },
            error: () => alert('讀取失敗!'),
        }
    )
}

function drawPM25() {
    $.ajax(
        {
            url: '/pm25-data',
            type: 'post',
            dataType: 'json',
            success: (data) => {
                console.log(data);
                // 指定图表的配置项和数据
                const option = {
                    title: {
                        text: '全台PM2.5資訊'
                    },
                    tooltip: {},
                    legend: {
                        data: ['PM2.5']
                    },
                    xAxis: {
                        data: data['site']
                    },
                    yAxis: {},
                    series: [
                        {
                            name: 'pm2.5',
                            type: 'bar',
                            data: data['pm25']
                        }
                    ]
                };
                chart1.setOption(option);

                $('#date').html(`<b>${data['date']}</b>`) //日期時間
                $('#pm25_high_site').text(data['highest'][0]); //jquery寫法
                document.querySelector('#pm25_high_value').innerText = data['highest'][1];//javascript寫法
                $('#pm25_low_site').text(data['lowest'][0]);
                document.querySelector('#pm25_low_value').innerText = data['lowest'][1];


            },
            error: () => alert('讀取失敗!'),
        }
    )
}