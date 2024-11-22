import os
import sys
import pandas as pd
from src.exception import customexception
from src.logger import logging
from utils.utils import load_object

class PredictPipeline():

    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join("artifacts","preprocessor.pkl")
            model_path=os.path.join("artifacts","model.pkl")

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            scaled_fea=preprocessor.transform(features)
            pred=model.predict(scaled_fea)

            return pred

        except Exception as e:
            raise customexception(e,sys)
        

class CustomData:
    def __init__(self):
        pass

    def get_data_as_dataframe(self):
        pass