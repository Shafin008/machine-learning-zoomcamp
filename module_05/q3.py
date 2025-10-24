'''
Question 3

We have prepared a pipeline with a dictionary vectorizer and a model. And then saved with Pickle. 

Download it from: curl -O https://github.com/DataTalksClub/machine-learning-zoomcamp/raw/refs/heads/master/cohorts/2025/05-deployment/pipeline_v1.bin

Let's use the model!

- Write a script for loading the pipeline with pickle
- Score this record:
{
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}
What's the probability that this lead will convert?
- 0.333
- 0.533
- 0.733
- 0.933
'''
import pickle
import os
from typing import Dict

# Checking if the file exists or not
# file_path = 'pipeline_v1.bin'
# if os.path.exists(file_path):
#     file_size = os.path.getsize(file_path)
#     print(f"File exists. Size: {file_size} bytes")
#     if file_size == 0:
#         print("File is empty!")
# else:
#     print("File doesn't exist!")


# Loading the pipeline (model)
with open('pipeline_v1.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

# Customer record
record = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

def pred_prob(record: Dict):
    prediction_probability = pipeline.predict_proba(record)[0, 1]
    return prediction_probability

if __name__ == "__main__":
    pp = pred_prob(record)
    print(pp)

