#━━━━━━━━━❮Bibliotecas❯━━━━━━━━━
import numpy as np
import pandas as pd
import joblib
from flask import Flask, request, render_template
#━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━


app = Flask(__name__)

rf_model = joblib.load('model')

#━━━━━━❮Função Produto❯━━━━━━━
def pred_churn(TotalCharges,MonthlyCharges, tenure):


    pred_val = rf_model.predict_proba([[TotalCharges, MonthlyCharges, tenure]])
    prob_churn = pred_val[0][1]
    if prob_churn < 0.25:
        return('Chance Quase Nula de Churn')
    elif prob_churn > 0.25 and prob_churn < 0.50:
        return('Pouca Chance de Churn')
    elif prob_churn > 0.50 and prob_churn < 0.60:
        return('Chance Moderada de Churn')
    elif prob_churn > 0.60 and prob_churn < 0.75:
        return('Chance Alta de Churn')
    elif prob_churn > 0.75:
        return('Chance Extrema de Churn')



#━━━━━━━━━❮Endpoints❯━━━━━━━━━
@app.route('/hello', methods=['GET'])
def HelloWorld():
    return 'Hello World'

@app.route('/', methods=['GET', 'POST'])
def home():
    pred = None
    if request.method == 'POST':
        TotalCharges = np.float(request.form.get('TotalCharges'))
        MonthlyCharges = np.float(request.form.get('MonthlyCharges'))
        tenure = np.float(request.form.get('tenure'))
        pred = pred_churn(TotalCharges,MonthlyCharges, tenure)
    return render_template('index.html', pred=pred)
#━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━

if __name__ == '__main__':
    app.run(debug=True)