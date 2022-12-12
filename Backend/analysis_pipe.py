import pandas as pd 
import json
 
# Opening JSON file

def ageGrp(data,min,max):
    count = 0
    for i in range(1, 70):
    
        if data[str(i)]['Age'] is not None:           
            if data[str(i)]['Age']>=min and data[str(i)]['Age']<max:
                count +=1
    return count

def diagnosisAge(data,dia,mi,ma):
    count = 0
    for i in range(1, 70):
        if dia in data[str(i)]['Diagnosis']:
            if data[str(i)]['Age'] is not None:           
                if int(data[str(i)]['Age'])>=mi and int(data[str(i)]['Age'])<ma:
                    count +=1
    return count

def getAgeGrpCount(data):
    age_count={}
    agegrp =["0-20","20-40","40-60","60-80","80-100"]

    b=0
    for i in range(4):
        age_count[agegrp[i]]=ageGrp(data,b,b+20)
        b+=20
    return age_count

def sexCount(data):
    count_m=0
    count_f=0
    for i in range(1, 70):#data.shape[1]
    
        if data[str(i)]['Sex'] is not None:           
            if data[str(i)]['Sex']=="M":
                count_m +=1
            elif data[str(i)]['Sex']=="F":
                count_f +=1
    d ={}
    d["count_m"]=count_m
    d["count_f"]=count_f
    return d





def sex_no(data):
    sex_count ={
        "M": sexCount(data)[0],
        "F": sexCount(data)[1]
    }
    return sex_count

def getDCA(data):
    diag={}
    for i in range(1, 70):
        
        for j in range(len(data[str(i)]['Diagnosis'])):
            b=0
            if data[str(i)]['Diagnosis'][j] not in diag:
                for k in range(4):
                    count = diagnosisAge(data,data[str(i)]['Diagnosis'][j],b,b+20)

                    diag.update({data[str(i)]['Diagnosis'][j]:[count,(b,b+20)]})
                    b+=20
    
    return diag


def driver():
    with open('finaldata-1.json') as json_file:
        data = json.load(json_file)
    data = pd.DataFrame.from_dict(data)
    for i in range(1,70):
            if data[str(i)]['Age'] is not None:
                data[str(i)]['Age'] = int(data[str(i)]['Age'][:2])

    return data


