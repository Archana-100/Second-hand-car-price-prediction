# -*- coding: utf-8 -*-
"""
check all request
send json data to api for predict car price
@author: archa
"""
import requests
import json
#API_ENDPOINT = "http://127.0.0.1:9090/predict"
API_ENDPOINT = "http://127.0.0.1:9090/car_price_prediction"
raw_dict = {
            'company':'Maruti',
            'name':'Maruti Suzuki Swift', 
            'year':2015, 
            'fuel_type':'LPG',
            'kms_driven':50000 
            }
r = requests.get(url = API_ENDPOINT,json =raw_dict)#json.dumps(raw_dict))
print(r.text)
print("result :%s"%r)

r2 = requests.post(url = API_ENDPOINT,json =raw_dict)
print(r2.text)
print("result :%s"%r2)

