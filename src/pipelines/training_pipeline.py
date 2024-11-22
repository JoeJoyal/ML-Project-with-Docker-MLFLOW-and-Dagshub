import os
import sys
import pandas as pd
from src.logger import logging
from src.exception import customexception

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation


obj=DataIngestion()

train_data_path,test_data_path=obj.initate_data_ingestion()

data_transformation=DataTransformation()

train_arr,test_arr=data_transformation.initialize_data_transformation(train_data_path, test_data_path)

model_trainer_obj=ModelTrainer()
model_trainer_obj.initate_data_model_trainer(train_arr,test_arr)
