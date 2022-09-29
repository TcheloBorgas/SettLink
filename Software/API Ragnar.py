import joblib
import numpy as np
import pandas as pd
import json
import os
from flask import Flask, request, render_template


app = Flask(__name__)

NeuralNet = joblib.load('pred')

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

if __name__ == '__main__':
    app.run(debug=True)