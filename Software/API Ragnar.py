#━━━━━━━━━❮Bibliotecas❯━━━━━━━━━
import joblib
import numpy as np
import pandas as pd
import json
import os
from flask import Flask, request, render_template
#━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━

app = Flask(__name__)

predict = joblib.load('pred')

#━━━━━━❮Função Produto❯━━━━━━━
def pred(gender,SeniorCitizen,Partner,Dependents,
         tenure,PhoneService,MultipleLines,InternetService,
         OnlineSecurity,DeviceProtection,TechSupport,StreamingTV,
         StreamingMovies,Contract,PaperlessBilling,PaymentMethod,
         MonthlyCharges,TotalCharges,Churn):


    previsao =NeuralNet.predict(pred)
    if previsao <0.25:
        print('Chance Quase Nula de Churn')
    elif previsao >0.25 and previsao <0.50:
        print('Pouca Chance de Churn')
    elif previsao >0.50 and previsao <0.60:
        print('Chance Moderada de Churn')
    elif previsao >0.60 and previsao <0.75:
        print('Chance Alta de Churn')
    elif previsao >0.75:
        print('Chance Extrema de Churn')


def previcaoN(temperature, humidity, ph, rainfall, label):
  x = [temperature, humidity, ph, rainfall, label]
  x = np.array(x)
  x = x.reshape([1,5])
  predY = rfN.predict(x)
  return predY

def previcaoP(temperature, humidity, ph, rainfall, label):
  x = [temperature, humidity, ph, rainfall, label]
  x = np.array(x)
  x = x.reshape([1,5])
  predY = rfP.predict(x)
  return predY

def previcaoK(temperature, humidity, ph, rainfall, label):
  x = [temperature, humidity, ph, rainfall, label]
  x = np.array(x)
  x = x.reshape([1,5])
  predY = rfK.predict(x)
  return predY


#━━━━━━━━━❮Endpoints❯━━━━━━━━━
@app.route('/hello', methods=['GET'])
def HelloWorld():
    return 'Hello World'

@app.route('/', methods=['GET', 'POST'])
def home():
    pred = None
    if request.method == 'POST':
        x1 = np.float(request.form.get('x1'))
        x2 = np.float(request.form.get('x2'))
        x3 = np.float(request.form.get('x3'))
        x4 = np.float(request.form.get('x4'))
        x5 = np.float(request.form.get('x5'))
        
        predN = previcaoN(x1, x2, x3, x4, x5)
        predP = previcaoP(x1, x2, x3, x4, x5)
        predK = previcaoK(x1, x2, x3, x4, x5)

        return render_template('index.html', predN = f"{predN[0]:.2f}", 
        predP = f"{predP[0]:.2f}", predK = f"{predK[0]:.2f}")
    return render_template('index.html')
    


@app.route('/predict', methods=['POST'])
def predict():
    event = json.loads(request.data)
    values = event['values']
    values = list(map(np.float, values))
    pred = iris(*values)
    return pred
#━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━




        
#━━━━━━━━━❮Endpoints❯━━━━━━━━━
@app.route('/Churn', methods=['GET', 'POST'])
def categ():
    x1 = np.str(request.form.get('x1'))
    pred = classificacaoCarreira(x1)
    return render_template('index.html', pred=pred)

@app.route('/numcand', methods=['GET', 'POST'])
def numcand():
    x2 = np.float(request.form.get('x2'))
    pred2 = pred(x2)
    return render_template('index.html', pred=pred2)
#━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━


if __name__ == '__main__':
    app.run(debug=True)