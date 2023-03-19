import sys
from src.logger import logging

def get_error_message(error, error_detail:sys):
    _,_, error_tb = error_detail.exc_info()
    file_name = error_tb.tb_frame.f_code.co_filename
    line_no = error_tb.tb_lineno
    error = str(error)
    error_message = 'The error occurred in python script [{0}] in line [{1}] and the error is: [{2}]'.format(file_name, line_no,error)
    return error_message


class CustomException(Exception):

    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = get_error_message(error_message,error_detail)

    def __str__(self):
        return self.error_message
    
    if __name__=='__main__':
        try:
            a = 1/0
        except Exception as e:
            logging.info('Division by zero')
            raise CustomException(e, sys)

