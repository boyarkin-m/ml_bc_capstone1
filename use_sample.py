import pickle
import numpy as np

import xgboost as xgb


def predict_single(customer, dv, model):
    X = dv.transform([customer])
    d = xgb.DMatrix(X, feature_names=features)

    y_pred = model.predict(d)
    return y_pred[0]


with open('subscribe-model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)
features = dv.get_feature_names()


customer = {'age': 29,
 'job': 'services',
 'marital': 'married',
 'education': 'high.school',
 'default': 'unknown',
 'housing': 'yes',
 'loan': 'no',
 'contact': 'cellular',
 'month': 'may',
 'day_of_week': 'thu',
 'campaign': 1,
 'pdays': 999,
 'previous': 1,
 'poutcome': 'failure',
 'emp.var.rate': -1.8,
 'cons.price.idx': 92.893,
 'cons.conf.idx': -46.2,
 'euribor3m': 1.266,
 'nr.employed': 5099.1}
    

prediction = predict_single(customer, dv, model)

print('prediction: %.3f' % prediction)

if prediction >= 0.5:
    print('verdict: Churn')
else:
    print('verdict: Not churn')