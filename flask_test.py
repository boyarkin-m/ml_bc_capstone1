import requests
import json

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

url = 'http://localhost:9696/predict'
response = requests.post(url, json=customer)
result = response.json()

print(json.dumps(result, indent=2))