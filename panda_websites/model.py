import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle
import requests
import json
import time


def fetch():
    data = requests.get('http://ec2-54-213-178-139.us-west-2.compute.amazonaws.com:3000/')
    data = data.text
    return json.loads(data)

def write(data):
    with open('cars-orig.csv', 'a') as f:

        line = f"{data['mpg']}, {data['cylinders']}, 0, {data['horsepower']}, {data['weight']}, 0, 0, 0, 0\n"
        f.write(line)


def train():
    df = pd.read_csv('cars-orig.csv')
    y = df.mpg
    X = df[['cylinders', 'horsepower', 'weight']]
    model = LinearRegression()
    model.fit(X,y)
    pickle.dump(model, open('linreg.p', 'wb'))


def reload():
    requests.get('http://localhost:3333/reload')

if __name__ == '__main__':
    while True:
        data = fetch()
        write(data)
        train()
        reload()
        time.sleep(1)
        print(data)

#
# df = pd.read_csv('cars-orig.csv')
#
# y = df['mpg']
# X = df[['cylinders', 'horsepower', 'weight']]
#
# model = LinearRegression()
# model.fit(X,y)
#
# pickle.dump(model, open('linreg.p', 'wb'))
