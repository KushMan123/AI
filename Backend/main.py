
from pymongo import MongoClient
import json



client  = MongoClient('localhost',27017)

db = client.flask_db  #database name
medical_data = db.medical_data #creating collectionss
with open("finaldata-1.json",'r') as f:
    data = json.load(f)


data_dic = [v for v in data.values()]
# print(data_dic)
x = medical_data.insert_many(data_dic)
# medical_data.drop()
print(medical_data.find_one())