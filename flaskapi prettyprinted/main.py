from flask import Flask
from flask import json
from flask.globals import request
from flask.json import jsonify
from flask.wrappers import Response
import requests

app = Flask(__name__)
names = [{"name":"shubham"},                                                    
         {"name":"akshay"},                                                    
         {"name":"amol"},                                                    
         {"name":"suraj"},                                                                                                        
         {"name":"saurabh"},                                                    
         {"name":"swastik"},                                                    
         {"name":"vaibhav"},                                                    
         {"name":"pratik"}]                         

@app.route('/')                                                    
def index():                                                    
    return jsonify({"message":"Welcome! Home!"})       


@app.route('/name',methods=['GET'])                                                    
def get_all():                                                  
    return jsonify({"data":names})      

@app.route('/name/<string:name>',methods=['POST'])                                                    
def add_name(name):                                                    
    new_name = {"name":name}                                                    
    names.append(new_name)                                                    
    print(names)                                                    
    return jsonify(new_name)                 

@app.route('/name/<string:name>',methods=['PUT'])
def edit_name(name):

    resp = request.json["name"]

    print(resp)
    try:
        for n  in names:
            if n["name"] == name:
                n['name'] = resp
    
        return jsonify({"message":f"successfully changed "},
                        {"data":names})
    except:
        return "Invalid Input"
    
@app.route('/name/<string:name>',methods=['DELETE'])
def delete_name(name):

    try:
        checks = [n for n in names if n["name"]==name]

        return jsonify({"message":"Welcome! Home!"},
                        {"data":checks})
    except:
        return "Invalid inputs"

if __name__ == "__main__":
    app.run(debug=True)


