# we will make an api here using flask
# and then we will make some function to handle our data and pridict 

from flask import Flask, request, jsonify
import numpy as np
import joblib
import json
from sklearn.preprocessing import LabelEncoder, StandardScaler
import pickle


scaler=joblib.load("../model/scaler.pkl")

en_model=joblib.load("../model/en_model.pkl")


def encode_data(data):
    """
    This function will encode the data
    """
    for column in data.columns:
        if data[column].dtype == "object":
            data[column] = le.fit_transform(data[column])
        else:
            pass
    return data

def scale_data(data):
    """
    This function will scale the data
    """
    data = scaler.transform(data)
    return data

def predict(data):
    """
    This function will predict the data
    """
    data = encode_data(data)
    data = scale_data(data)
    prediction = en_model.predict(data)
    return prediction

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_route():
    """
    This function will handle the post request
    """
    data = request.get_json()
    data = pd.DataFrame(data, index=[0])
    prediction = predict(data)
    return jsonify({"prediction": list(prediction)})

if __name__ == "__main__":
    app.run(debug=True)

# Now we will run this file and then we will make a post request to this api and then we will get the prediction
# we can use postman to make the post request
# we will make a post request to the url http://
# and then we will pass the data in
