import sys

def get_error_message(error, error_detail:sys):
    _,_, error_tb = error_detail.exc_info()
    file_name = error_tb.tb_frame.f_code.co_filename
    line_no = error_tb.tb_lineno
    error = str(error)
    error_message = 'The error occurred in python script [{0}] in line [{1}] and the error is: [{2}]'.format(file_name, line_no,error)
    return error_message


def CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        
        # that is we will pass the error message and with that error message, an instance of exception class is created
        super().__init__(error_message)
        self.error_message = get_error_message(error_message,error_detail)

    def __str__(self):
        return self.error_message

