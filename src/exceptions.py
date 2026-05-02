import sys

def error_message_detail(error, error_detail: sys):
    # exc_tb contains the traceback (file name, line number, etc.)
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    
    # Formulated error message
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, line_number, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        # Capture the detailed error using the function above
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        # This ensures that when we print the exception, we see our detailed message
        return self.error_message


