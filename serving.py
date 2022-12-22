import pickle
import numpy as np

import xgboost as xgb

from flask import Flask, request, jsonify

def predict_single(customer, dv, model):
    X = dv.transform([customer])
    d = xgb.DMatrix(X, feature_names=features)

    y_pred = model.predict(d)
    return y_pred[0]


with open('subscribe-model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)
features = dv.get_feature_names()

app = Flask('churn')


@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    
    prediction = predict_single(customer, dv, model)
    churn = prediction >= 0.5
    
    result = {
        'subscribe_probability': float(prediction),
        'subscribe': bool(churn),
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)