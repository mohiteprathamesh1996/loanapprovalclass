import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('build_pipeline.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    
    rescap = pd.DataFrame(
      int_features,
      index=[
        'Loan_ID', 'Gender', 'Married', 'Dependents', 'Education',
        'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
        'Loan_Amount_Term', 'Credit_History', 'Property_Area'
        ]
        ).T

    rescap[['ApplicantIncome',
     'CoapplicantIncome',
     'LoanAmount',
     'Loan_Amount_Term',
     'Credit_History']] = rescap[['ApplicantIncome',
     'CoapplicantIncome',
     'LoanAmount',
     'Loan_Amount_Term',
     'Credit_History']].astype(float)

    output = model.predict(rescap)[0]

    if output=="Y":
      status = "Approved"
    else:
      status = "Rejected"

    return render_template(
      'index.html', 
      prediction_text='Loan Appication Status : {}'.format(
        status
        )
      )



if __name__ == "__main__":
    app.run(debug=True)
