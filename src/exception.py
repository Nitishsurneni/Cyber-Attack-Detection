import sys

def error_message_detail(error, detail: sys):
    """
    Returns a detailed error message.
    
    Args:
        error: The exception object.
        detail: The sys module for accessing exception information.
    
    Returns:
        str: A formatted error message.
    """
    _, _, exc_tb = detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    return f"Error occurred in script: [{file_name}] at line number: [{line_number}] with message: [{str(error)}]"

class CustomException(Exception):
    """
    Custom exception class that captures detailed error information.
    
    Args:
        error: The exception object.
        detail: The sys module for accessing exception information.
    """
    def __init__(self, error, detail: sys):
        super().__init__(error_message_detail(error, detail))
        self.error = error
        self.detail = detail
    def __str__(self):
        return self.error_message_detail(self.error, self.detail)