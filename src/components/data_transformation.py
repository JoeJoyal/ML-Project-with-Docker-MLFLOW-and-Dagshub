import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path
from dataclasses import dataclass

from src.logger import logging
from src.exception.exception import customexception
from src.utils.utils import save_object

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler




@dataclass
class DataTransformationConfig:
    pass

class DataTransformationConfig:
    def __init__(self):
        pass

    def initate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)