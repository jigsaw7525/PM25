from flask import Flask, render_template, request
from datetime import datetime
from pm25 import get_pm25
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
    return render_template('pm25-charts.html')


@app.route('/pm25-data', methods=["GET", "POST"])
def get_pm25_data():
    columns, values = get_pm25()

    site = [value[1] for value in values]
    pm25 = [value[2] for value in values]

    data = {'site': site, 'pm25': pm25}
    print(data)
    return json.dumps(data, ensure_ascii=False)


if __name__ == "__main__":
    app.run(debug=True)
