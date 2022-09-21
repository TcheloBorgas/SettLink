import joblib
import numpy as np
import pandas as pd
import json
import os
from flask import Flask, request, render_template

PEOPLE_FOLDER = os.path.join('static', 'flowers')


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

model = joblib.load('logistic_model')

def iris(sepal_length,	sepal_width, petal_length,petal_width):
    data = np.array(['setosa', 'versicolor', 'virginica'])
    x = np.array([sepal_length,	sepal_width, petal_length,petal_width	])
    x = x.reshape((1,4))
    x = pd.DataFrame(x, columns=['sepal length (cm)',
    'sepal width (cm)',
    'petal length (cm)',
    'petal width (cm)'])
    flor =  model.predict(x)[0]
    return data[flor]

@app.route('/hello', methods=['GET'])
def HelloWorld():
    return 'Hello World'

@app.route('/', methods=['GET', 'POST'])
def home():
    pred = None
    if request.method == 'POST':
        sl = np.float(request.form.get('sl'))
        sw = np.float(request.form.get('sw'))
        pl = np.float(request.form.get('pl'))
        pw = np.float(request.form.get('pw'))
        pred = iris(sl,sw,pl,pw)

    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], f'{pred}.jpg')
    # return render_template("index.html", full_image = full_filename)
    return render_template('index.html', pred=pred, full_image = full_filename)

@app.route('/predict', methods=['POST'])
def predict():
    event = json.loads(request.data)
    values = event['values']
    values = list(map(np.float, values))
    pred = iris(*values)
    return pred

if __name__ == '__main__':
    app.run(debug=True)

