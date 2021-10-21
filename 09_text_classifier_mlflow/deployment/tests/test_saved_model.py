# coding=utf-8

import pandas as pd
from mlflow import pyfunc
import mlflow
import os

os.chdir("classifier/")

test_model = mlflow.sklearn.load_model(".")

test_inputs = ["Please enlighten me.  How is omnipotence contradictory"]

prediction = test_model.predict(test_inputs)

print(prediction)