import os
import sys
import pickle
import numpy as np
import pandas as pd
import mlflow
import mlflow.sklearn
from urllib.parse import urlparse
from pathlib import Path
from dataclasses import dataclass

from src.logger import logging
from src.exception import customexception
from src.utils.utils import save_object

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error


@dataclass
class ModelEvaluationConfig:
    pass

class ModelEvaluation:
    def __init__(self):
        pass

    def initate_data_model_evaluation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)