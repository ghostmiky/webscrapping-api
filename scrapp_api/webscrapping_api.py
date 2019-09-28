# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:40:46 2019

@author: User
"""


import webscrapper3 as w3
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from flask import jsonify

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

def verify_scrapped_data(receivedData):
    if ('text' not in receivedData):
        return 300
    else:
        return 200


class scrapp_api(Resource):
    def post(self):
        receivedData = request.get_json() # Receieve data
        status_code = verify_scrapped_data(receivedData) # Verify data
        if (status_code != 200):
            returnJson = {
            	'msg': 'Invalid data',
                'status': 200
            }
            return jsonify(returnJson)
        text = receivedData['text']
       	url = f"""{text}"""
        url = url 
        try:
            ws = w3.webscrapp()
            res =ws.scrapp(url)
        	
            returnJson = {
            	'result': res,
            	'status': 200 
	        }
            return jsonify(returnJson) 
        except Exception as e:
        	returnJson = {
            	'msg': e,
            	'status': 500
        	}
        	return jsonify(returnJson)
        

api.add_resource(scrapp_api,'/scrap/')

if __name__ == '__main__':
    app.run()
    
# Home route
@app.route('/api')
def welcome():
    return 'WebScrapping API'