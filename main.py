from flask import Flask,render_template,request,url_for,redirect
from werkzeug.utils import secure_filename
import json
import pandas as pd

with open('configs.json', 'r') as c :
    params = json.load(c)["params"]

with open('VehiclesAPI/Vehicledata.json', 'r') as m : 
    data = json.load(m) 
app = Flask(__name__)

@app.route("/")
def home():
    #print(data)
    return render_template('index.html',jsdata=data,params=params)


@app.route("/truck_id", methods=['GET'])
def truck_id():
    a=request.values.get('truck_input')
    data1=data.get("Fleet")
    data2=pd.DataFrame(data1)
    if a is not None:
        cities = []
        for i, each in enumerate(data2['Truck']):
            if each['id']==a.strip():
                cities.append(i)
        data3=data2.iloc[cities,:]
        return render_template('truck_id.html',params=params,data=data3)
    return render_template('truck_id.html',params=params,data=data2)
    


@app.route("/truck_id_name",methods=['GET'])
def truck_id_name():
    a=request.values.get('truck_name_input')
    data1=data.get("Fleet")
    data2=pd.DataFrame(data1)
    if a is not None:
        cities = []
        for i, each in enumerate(data2['Truck']):
            if (each['name']).lower()==a.lower().strip():
                cities.append(i)
        data3=data2.iloc[cities,:]
        return render_template('truck_name.html',params=params,data=data3)
    return render_template('truck_name.html',params=params,data=data2)

@app.route("/truck_id_driver",methods=['GET'])
def truck_id_driver():
    a=request.values.get('driver_input')
    data1=data.get("Fleet")
    data2=pd.DataFrame(data1)
    if a is None:
        return render_template('truck_driver.html',data=data2,params=params)
    data3=data2[data2["driver"].str.lower()==a.lower().strip()]
    return render_template('truck_driver.html',data=data3,params=params)

app.run(debug=True)