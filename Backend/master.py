from flask import Flask
from flask_pymongo import PyMongo
from flask import request
from flask.json import jsonify
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/flask_db"
mongo = PyMongo(app)


@app.route("/")
def hello():
    data =  mongo.db.medical_data.find({})
   
    dic = {}
    for i,d in enumerate(data):
        dic[i] = d
        dic[i]["_id"] = str(dic[i]["_id"])
    return  dic

@app.route("/filter")
def filter():
   
    age = request.args.get('Age')
    diagnosis = request.args.get('Diagnosis')
    pre_medication = request.args.get('Pre_Medication')
    sex = request.args.get('Sex')
    test = request.args.get('Test')
    symptoms = request.args.get('Symptoms')
    treatment = request.args.get('Treatment')
    # age ="75-years-old"
    query ={}
    query['$and']=[]
    if age:
        query['$and'].append({"Age":{"$regex":age}})
    if diagnosis:
        query['$and'].append({"Diagnosis":{"$regex":diagnosis}})
    if pre_medication:
        query['$and'].append({"Pre_Medication":{"$regex":pre_medication}})
    if sex:
        query['$and'].append({"Sex":{"$regex":sex}})
    if test:
        query['$and'].append({"Test":{"$regex":test}})
    if symptoms:
        query['$and'].append({"Symptoms":{"$regex":symptoms}})
    if treatment:
        query['$and'].append({"Treatment":{"$regex":treatment}})


    if len(query["$and"]) ==0:
        data =  mongo.db.medical_data.find({})

    else:
        data =  mongo.db.medical_data.find(query)

    
    dic = {}
    for i,d in enumerate(data):
            dic[i] = d
            dic[i]["_id"] = str(dic[i]["_id"])
    
    return dic

# @app.route("/h")
# def h():
#     data = 

import pandas as pd 
import json
from analysis_pipe import *

data = driver()

@app.route("/Vis/age")
def age():
    d = getAgeGrpCount(data)
    return d

@app.route("/Vis/sex")
def sex_count():
    d = sexCount(data)
    print(d)
    return d

@app.route("/Vis/dca")
def value_DCA():
    d=getDCA(data)
    return d


 




# main driver function
if __name__ == '__main__':
    app.run()