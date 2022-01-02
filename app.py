import os
from flask import Flask,render_template,send_from_directory,request
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/getdata', methods=['GET','POST'])
def getdata():
    if request.method == 'POST':
        fromdate = request.form.get('fromdate')
        todate = request.form.get('todate')
        dimensions = request.form.get('dimensions')
        metrices = request.form.get('metrices')
        print(fromdate, todate, dimensions, metrices)
    return 'submitted successfully'



@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')



if __name__ == "__main__":
    app.run(debug = True)