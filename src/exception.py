import sys
from src.logger import logging

def error_message_details(err_msg, err_details:sys):
    _,_, exec_tb =  err_details.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    line_number = exec_tb.tb_lineno

    error_message = f"Error occured in python script name [{file_name}] line number [{line_number}] error message[{str(err_msg)}]"
    return error_message


class CustomException(Exception):
    def __init__(self, err_msg, err_details:sys):
        super().__init__(err_msg)
        self.error_message = error_message_details(err_msg, err_details)

    def __str__(self):
        return self.error_message
    

