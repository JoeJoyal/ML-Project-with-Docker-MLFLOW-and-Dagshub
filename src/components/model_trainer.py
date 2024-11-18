import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path
from dataclasses import dataclass

from src.logger import logging
from src.exception.exception import customexception
from src.utils.utils import save_object

from sklearn.linear_model import LinearRegression, Ridge

@dataclass
class ModelTrainerConfig:
    pass

class ModelTrainer:
    def __init__(self):
        pass

    def initate_data_model_trainer(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)