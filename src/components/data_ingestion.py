import os
import sys
from src.exceptions import CustomException
from src.logger import logging
import numpy as np
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split


@dataclass
class DataIngestionConfig:
    train_data_path : str =os.path.join('artifacts','train_data')
    test_data_path : str =os.path.join('artifacts','test_data')
    raw_data_path : str =os.path.join('artifacts','raw_data')

class DataIngestion:
    def __init__(self):
        self.ingestionconfig = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info('Data Ingestion started')
        try:

            # Making the folders for saving the data:
            os.makedirs(os.path.dirname(self.ingestionconfig.train_data_path),exist_ok=True)
            os.makedirs(os.path.dirname(self.ingestionconfig.test_data_path),exist_ok=True)
            os.makedirs(os.path.dirname(self.ingestionconfig.raw_data_path),exist_ok=True)
            
            # Reading the data
            df = pd.read_csv('notebook\data\ANDRIOD AUTHENTICITY PREDICTION.csv')
            logging.info('Read the Data')
            
            train_data, test_data = train_test_split(df, test_size =0.2, random_state=40 )
            logging.info('Train test split done')

            # df.to_csv(self.ingestionconfig.raw_data_path)
            # train_data.to_csv(self.ingestionconfig.train_data_path)
            # test_data.to_csv(self.ingestionconfig.test_data_path)
            logging.info('Ingestion of data is completed')

            return (self.ingestionconfig.train_data_path, self.ingestionconfig.test_data_path)
        except Exception as e:
            raise CustomException(e,sys)


            
