import os
import sys
from dataclasses import dataclass
from src.exceptions import CustomException
from src.logger import logging

from src.utils import save_object, evaluate_models

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn.naive_bayes import MultinomialNB


from sklearn.metrics import recall_score

@dataclass
class Model_trainer_config:
    model_path = os.path.join('artifacts','model.pkl')

@dataclass
class ModelTraining:
    model_trainer_config = Model_trainer_config()

    def initiate_model_training(self, train_arr, test_arr):
        try:
            logging.info('dependent and independent df creating')
            X_train = train_arr[:,:-1]
            y_train = train_arr[:,-1]
            X_test = test_arr[:,:-1]
            y_test = test_arr[:,-1]

            models = {'KNN' : KNeighborsClassifier(),
                      'SVC': SVC(),
                      'Random Forest': RandomForestClassifier(),
                      'Gradient Boosting': GradientBoostingClassifier(),
                      'MultinomialNB': MultinomialNB()
                      }
            params = {'KNN' : {'n_neighbors' :list(range(1,30)), 
                                'metric'  : ['minkowski','euclidean','manhattan']},
                        'SVC': {'C':[1.0],
                               'kernel':['rbf'] },

                      'Random Forest': {'n_estimators':[100,120,130], 
                                        'max_depth':[3, 5, 7]},

                      'Gradient Boosting': {'n_estimators':[50, 80,  100], 
                                            'max_depth':[3, 5, 7]},
                        'MultinomialNB': {'alpha':[1.0]}
                      }
            model_report : dict = evaluate_models(X_train, y_train, X_test, y_test, models, params)

            best_model_score = max(sorted(model_report.values()))
            best_model_name = dict(zip(model_report.values(),model_report.keys()))[best_model_score]
            best_model = models[best_model_name]

            if best_model_score< 0.7:
                raise CustomException('No model Found')
            logging.info('Best Found Model')

            save_object(file_path = self.model_trainer_config.model_path, obj= best_model)

            predicted = best_model.predict(X_test)
            recall = recall_score(predicted, y_test)
            return recall

        except Exception as e:
            raise CustomException(e, sys)

    



