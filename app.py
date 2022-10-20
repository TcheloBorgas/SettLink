#━━━━━━━━━❮Bibliotecas❯━━━━━━━━━
import numpy as np
import pandas as pd
import json
import os
from flask import Flask, request, render_template
from tensorflow import keras
#━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━


app = Flask(__name__)

predict = keras.models.load_model('model')

#━━━━━━❮Função Produto❯━━━━━━━
def pred_churn(gender,SeniorCitizen,Partner,Dependents,
         tenure,PhoneService,MultipleLines,InternetService,
         OnlineSecurity,DeviceProtection,TechSupport,StreamingTV,
         StreamingMovies,Contract,PaperlessBilling,PaymentMethod,
         MonthlyCharges,TotalCharges):

    print(gender,SeniorCitizen,Partner,Dependents,
         tenure,PhoneService,MultipleLines,InternetService,
         OnlineSecurity,DeviceProtection,TechSupport,StreamingTV,
         StreamingMovies,Contract,PaperlessBilling,PaymentMethod,
         MonthlyCharges,TotalCharges)


'''    previsao =NeuralNet.predict(pred)
    if previsao <0.25:
        print('Chance Quase Nula de Churn')
    elif previsao >0.25 and previsao <0.50:
        print('Pouca Chance de Churn')
    elif previsao >0.50 and previsao <0.60:
        print('Chance Moderada de Churn')
    elif previsao >0.60 and previsao <0.75:
        print('Chance Alta de Churn')
    elif previsao >0.75:
        print('Chance Extrema de Churn')'''



#━━━━━━━━━❮Endpoints❯━━━━━━━━━
@app.route('/hello', methods=['GET'])
def HelloWorld():
    return 'Hello World'

@app.route('/', methods=['GET', 'POST'])
def home():
    pred = None
    if request.method == 'POST':
        gender = request.form.get('gender')
        
        InternetService = request.form.get('InternetService')
        
        Partner = request.form.get('Partner')
        
        Dependents = request.form.get('Dependents')
        
        PhoneService = request.form.get('PhoneService')
        
        MultipleLines = request.form.get('MultipleLines')
        
        OnlineSecurity = request.form.get('OnlineSecurity')
        
        OnlineBackup = request.form.get('OnlineBackup')
        
        DeviceProtection = request.form.get('DeviceProtection')
        
        TechSupport = request.form.get('TechSupport')
        
        StreamingTV = request.form.get('StreamingTV')
        
        StreamingMovies = request.form.get('StreamingMovies')
        
        Contract = request.form.get('Contract')
        
        PaymentMethod = request.form.get('PaymentMethod')
        
        PaperlessBilling = request.form.get('PaperlessBilling')
        
        SeniorCitizen = request.form.get('SeniorCitizen')
        
        tenure = request.form.get('tenure')

        MonthlyCharges = request.form.get('MonthlyCharges')
        
        TotalCharges = request.form.get('TotalCharges')
        
        pred_churn(gender,SeniorCitizen,Partner,Dependents,
                tenure,PhoneService,MultipleLines,InternetService,
                OnlineSecurity,DeviceProtection,TechSupport,StreamingTV,
                StreamingMovies,Contract,PaperlessBilling,PaymentMethod,
                MonthlyCharges,TotalCharges)

        return render_template('index.html')
    return render_template('index.html')
#━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━



if __name__ == '__main__':
    app.run(debug=True)