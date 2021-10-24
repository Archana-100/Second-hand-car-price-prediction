# -*- coding: utf-8 -*-
"""
check all request
send json data to api for predict car price
@author: archa
"""
import requests
import json
API_ENDPOINT = "http://127.0.0.1:9090/predict"
raw_dict = {
            'company':'Maruti',
            'name':'Maruti Suzuki Swift', 
            'year':2015, 
            'fuel_type':'LPG',
            'kms_driven':50000 
            }
r = requests.post(url = API_ENDPOINT,json =raw_dict)#json.dumps(raw_dict))
print("result :%s"%r)

