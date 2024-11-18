import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path
from dataclasses import dataclass

from src.logger import logging
from src.exception.exception import customexception


from sklearn.model_selection import train_test_split



@dataclass
class DataIngestionConfig:
    pass

class DataIngestion:
    def __init__(self):
        pass

    def initate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)