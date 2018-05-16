import sys
import pandas as pd
import pickle
from flask import Flask, render_template, request, jsonify, Response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '<h1> hello world </h1>'

@app.route('/version', methods=['GET'])
def version():
    return sys.version

@app.route('/square', methods=['POST'])
def square():
    req = request.get_json()
    x = req['x']

    print('the request was:', req)
    return jsonify({'x': x, 'x**2': x**2})


model = pickle.load(open('linreg.p', 'rb'))


@app.route('/inference', methods=['POST'])
def inference():
    req = request.get_json()
    c, h, w = req['cylinders'], req['horsepower'], req['weight']
    prediction = list(model.predict([[c,h,w]]))
    return jsonify({'c' : c, 'h' :h, 'w':w, 'prediction' : prediction[0]})

#
# @app.route('/panda.html', methods=['GET'])
# def about():
#     return render_template('panda.html')

@app.route('/home.php', methods=['GET'])
def about():
    return render_template('home.php')


@app.route('/mpg.php', methods=['GET'])
def mpg():
    return render_template('mpg.php')


@app.route('/faq.php', methods=['GET'])
def faq():
    return render_template('faq.php')

@app.route('/reload', methods=['GET'])
def reload():
    global model
    model = pickle.load(open('linreg.p', 'rb'))
    return 'OK'


@app.route('/plot', methods=['GET'])
def plot():
    df = pd.read_csv('cars-orig.csv')
    data = list(zip(df.mpg,df.weight))
    return jsonify(data)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=3333, debug=True)
