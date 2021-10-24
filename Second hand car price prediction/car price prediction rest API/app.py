# -*- coding: utf-8 -*-
"""
arch car price prediction API
@author: archna
"""
from flask import Flask,request,redirect
import pickle
import pandas as pd
import numpy as np

app=Flask(__name__)
model=pickle.load(open('carpricepredictionbyLR.pkl','rb'))
@app.route('/predict',methods=['POST'])
def predict():
    try:
        print("start")
        data=request.get_json()
        print(data)
        company_name = data["company"]
        car_model_name= data["name"]
        year=data["year"]
        fuel_type=data["fuel_type"]
        kms_driven=data["kms_driven"]
        prediction=model.predict(pd.DataFrame(columns=['name','company','year','kms_driven','fuel_type'],
                                  data=np.array([car_model_name,company_name,year,kms_driven,fuel_type]).reshape(1, 5)))
        print(prediction)
        predicted_car_price = str(np.round(prediction[0],2))
        return (predicted_car_price)
    except Exception as e:
        print(e)
        return e


if __name__=='__main__':
    app.run(port=9090)
    
    
"""data format for post 
url : "http://127.0.0.1:9090/predict"
data = {
            'name':'Maruti Suzuki Swift', 
            'company':'Maruti', 
            'year':2015, 
            'kms_driven':50000, 
            'fuel_type':'LPG'}"""