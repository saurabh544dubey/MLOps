import sys

### Whenever an exception gets raised, I want to push this on my own custom message

def error_message_detail(error,error_detail:sys):    ### error:whatever message I'm gettingk
    _,_,exc_tb=error_detail.exc_info() ## Execution info : exc_tb will give me all the details about Exception: which file,line
    
    ### File in which the error is occuring
    file_name=exc_tb.tb_frame.f_code.co_filename
    ### My custom error message
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    
    return error_message
    

### Making my own Custom Exception class
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail) ### error_detail will be tracked by sys
        
    def __str__(self):
        return self.error_message