import os
import sys
from src.exceptions import CustomException
from src.logger import logging
from src.utils import save_object, get_binary_encoded_columns

import numpy as np
import pandas as pd
from dataclasses import dataclass

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path:str = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        ''' This Function is responsible for data transformation.
        '''

        try:
            numerical_columns = ['Rating', 'Number of ratings','Price']
            categorical_columns = ['Category']
            binary_encoded_columns = get_binary_encoded_columns()
            num_pipeline = Pipeline(steps =[('num_imputer',SimpleImputer(strategy = 'median')),
                                            ('scaler',StandardScaler(with_mean=False))])
            category_pipeline = Pipeline(steps= [('category_imputer',SimpleImputer(fill_value = '',strategy ='constant')),
                                                ('onehotencoder', OneHotEncoder(handle_unknown='ignore'))])
            binary_pipeline = Pipeline(steps = [('binary_imputer',SimpleImputer(strategy='most_frequent'))])
            preprocessor = ColumnTransformer([('categorical',category_pipeline,categorical_columns),
                                              ('numerical',num_pipeline, numerical_columns),
                                              ('binary',binary_pipeline,binary_encoded_columns)])
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info('Read train and test data')
            logging.info('preprocessing object instantiation started')
            preprocessor_object = self.get_data_transformer_object()
            numerical_columns = ['Rating', 'Number of ratings','Price']
            categorical_columns = ['Category']
            binary_encoded_columns = get_binary_encoded_columns()
            features_list = categorical_columns + numerical_columns + binary_encoded_columns
            target_column = ['Class']
            input_feature_train_df = train_df[features_list]
            target_feature_train_df = train_df[target_column]

            input_feature_test_df = test_df[features_list]
            target_feature_test_df = test_df[target_column]
            logging.info('Applying preprocessing object on data')
            processed_train_df = preprocessor_object.fit_transform(input_feature_train_df)
            processed_test_df = preprocessor_object.transform(input_feature_test_df)

            train_arr = np.c_[processed_train_df, np.array(target_feature_train_df)]
            test_arr = np.c_[processed_test_df,np.array(target_feature_test_df)]

            logging.info('saved preprocessed object')

            save_object(file_path = self.data_transformation_config.preprocessor_obj_file_path,
                        obj = preprocessor_object)
            return (train_arr, test_arr,self.data_transformation_config.preprocessor_obj_file_path )
            

        except Exception as e:
            raise CustomException(e,sys)

