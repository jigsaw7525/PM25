from flask import Flask, render_template, request
from datetime import datetime
from pm25 import *
import json
app = Flask(__name__)


@app.route('/')
def index():
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    name = "wender"
    # **可以代表字典
    return render_template('./index.html', context={'name': name, 'date': date})


@app.route('/stocks')
def stock():
    all_stocks = [
        {'分類': '日經指數', '指數': '22,920.30'},
        {'分類': '韓國綜合', '指數': '2,304.59'},
        {'分類': '香港恆生', '指數': '25,083.71'},
        {'分類': '上海綜合', '指數': '3,380.68'}
    ]

    return render_template('./stock.html', stocks=all_stocks)


@app.route('/today/<name>')
def time(name):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'{name}<br/>{date}'


@app.route('/sum/x=<a>&y=<b>', methods=["GET"])
def get_sum(a, b):
    total = eval(a)+eval(b)
    return str(total)


@app.route('/bmi/<name>&height=<height>&weight=<weight>', methods=["GET"])
def get_bmi(name, height, weight):
    bmi = eval(weight)/((eval(height)/100)**2)
    return f'{name}<br/>{bmi}'


@app.route('/pm25', methods=["GET", "POST"])
def pm25():

    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    columns, values = get_pm25()

    if request.method == 'GET':
        columns, values = get_pm25()

    if request.method == 'POST':
        if request.form.get('reverse'):
            columns, values = get_pm25(type=1)
        elif request.form.get('ascending'):
            columns, values = get_pm25(type=2)

    return render_template("./pm25.html", columns=columns, values=values, date=date)


@app.route('/pm25-chart')
def pm25_chart():
    countys = get_county()
    return render_template('./pm25-charts.html', countys=countys)


@app.route('/county-pm25/<string:county>')
def get_county_json(county):
    datas = get_county_pm25(county)
    data = {
        'title': county,
        'county': [data[0] for data in datas],
        'pm25': [data[-1] for data in datas]
    }
    return json.dumps(data, ensure_ascii=False)


@app.route('/pm25-data', methods=["GET", "POST"])
def get_pm25_data():
    columns, values = get_pm25()

    site = [value[1] for value in values]
    pm25 = [value[2] for value in values]
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    datas = [[value[1], value[-1]]for value in values]
    datas = sorted(datas, key=lambda x: x[-1])

    data = {'site': site, 'pm25': pm25, 'date': date,
            'highest': datas[-1], 'lowest': datas[0]}
    print(data)
    return json.dumps(data, ensure_ascii=False)


@app.route('/six-data', methods=["GET", "POST"])
def get_six_json():
    datas = get_six_pm25()
    return json. dumps({'county': list(datas.keys()), 'pm25': list(datas.values())},
                       ensure_ascii=False)


if __name__ == "__main__":
    app.run(debug=True)
