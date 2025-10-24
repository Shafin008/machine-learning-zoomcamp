'''
Question 4
Now let's serve this model as a web service

- Install FastAPI
- Write FastAPI code for serving the model
- Now score this client using requests

What's the probability that this client will get a subscription?
- 0.334
- 0.534
- 0.734
- 0.934
'''
from fastapi import FastAPI
from typing import Dict, Any
from q3 import pred_prob

app = FastAPI(title="Lead Score V2")

@app.post('/predict')
def predict(record: Dict[str, Any]):
    pp = pred_prob(record)
    return {
        "Lead Score": pp,
        "Subs": bool(pp >= 0.5) 
    }