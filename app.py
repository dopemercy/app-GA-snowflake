import os
from flask import Flask, request, render_template, send_from_directory
from flask.templating import render_template
from config import cursor
import datetime

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/getdata', methods=['GET', 'POST'])
def getdata():
    if request.method == 'POST':
        fromdate = request.form.get('fromdate')
        todate = request.form.get('todate')
        dimensions = request.form.getlist('dimensions')
        metrices = request.form.getlist('metrices')
        startDate = datetime.datetime.strptime(fromdate, '%Y-%m-%d')
        endDate = datetime.datetime.strptime(todate, '%Y-%m-%d')
        val = dimensions + metrices
        values = ', '.join(val) 
        print(cursor.execute(
            f"select {values} FROM USERS WHERE DATES BETWEEN ? and ?", [startDate.date(), endDate.date()]).fetch_pandas_all())
    return 'submitted successfully'


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    app.run(debug=True)
