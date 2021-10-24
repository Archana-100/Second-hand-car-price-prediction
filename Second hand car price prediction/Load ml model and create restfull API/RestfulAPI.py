# -*- coding: utf-8 -*-
"""
create REstful API from machine learning model using flask
@author: archna gaikwad
"""
#import required packages
from flask import Flask, jsonify, request,Response
from flask_restful import Resource, Api
import pickle
import pandas as pd
import numpy as np

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

#load machine learning model 
model=pickle.load(open('carpricepredictionbyLR.pkl','rb'))

# sample_data={'name':'Maruti Suzuki Swift', 
#                         'company':'Maruti', 
#                         'year':2015, 
#                         'kms_driven':50000, 
#                         'fuel_type':'LPG'}

# making a class for a car data_requests resource
# they are automatically mapped by flask_restful.
class car_data(Resource):      
    def get(self): 
    
        try:
               car_info ={'name':'Maruti Suzuki Swift', 
                                    'company':'Maruti', 
                                    'year':2015, 
                                    'kms_driven':50000, 
                                    'fuel_type':'LPG'}
               return jsonify({"result":car_info,"status":"success"})
        except Exception as e:
            responce = {"result":e,"status":"fail"}
            return jsonify(responce)
    
    def post(self): 
        try:
            data=request.get_json()
            company_name = data["company"]
            car_model_name= data["name"]
            year=data["year"]
            fuel_type=data["fuel_type"]
            kms_driven=data["kms_driven"]
            prediction=model.predict(pd.DataFrame(columns=['name','company','year','kms_driven','fuel_type'],
                                      data=np.array([car_model_name,company_name,year,kms_driven,fuel_type]).reshape(1, 5)))
            #print(prediction)
            predicted_car_price = str(np.round(prediction[0],2))
            
            print(predicted_car_price)
           
            return jsonify({'predicted Car Price': predicted_car_price,"status":"success"})
        except Exception as e:
            responce = {"result":e,"status":"fail"}
            return jsonify(responce)
      
# adding the defined resources along with their corresponding urls
api.add_resource(car_data, '/car_price_prediction')

if __name__ == '__main__':
    app.run(port=9090)
