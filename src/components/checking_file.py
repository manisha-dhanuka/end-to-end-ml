from src.components.data_ingestion import DataIngestionConfig, DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.exceptions import CustomException
import sys
import os

if __name__ =='__main__':
    obj = DataIngestion()
    train , test = obj.initiate_data_ingestion()
    transformation = DataTransformation()
    train_arr,test_arr,_=transformation.initiate_data_transformation(train,test)
    

