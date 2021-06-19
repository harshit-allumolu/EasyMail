"""

Author : Harshit Allumolu <allumoluharshit@gmail.com>

Functionality : To generate an email template based on the excel file uploaded.

Idea : The idea is to facilitate users with a template generator rather than asking them to write an email all the way from scratch. 
The excel file containing email IDs is used for this purpose. A user can generate a template with editable fields for whatever columns in the excel sheet he/she wants.

Let's dive into the code for more details!

"""


# NOTE : This is a basic version of template generation without any language models
# TODO : Try to generate more realistic sentences for each column entry using language models


# import required modules
import pandas as pd

greetings = {
    True : "Hi",
    False : "Dear"
}

signatures = {
    True : "Yours sincerely",
    False : "Yours truly"
}

def generateTemplate(columnsList : list, formal : bool = True, greeting : bool = True, signature : bool = False, author : str = None) -> str:
    """    
        Function name : generateTemplate

        Arguments : 
            -- columnsList (list type) : A list containing all column names in the excel sheet. Mention only those columns which are needed in the template.
            -- formal (bool type) : A boolean flag for formal/informal type switch. (default = True)
            -- greeting (bool type) : A boolean flag to include or not the greeting line in the email template. (default = True)
            -- signature (bool type) : A boolean flag to indicate if bottom section of the email with your name is required or not. (default = False)
            -- author (str type) : The name of the person who is writing this email. This must be given if signature is True.

        Return :
            -- A template which is of type str
    """
    template = ""
    # three parts in a template
    # part 1 : greeting
    if greeting:
        template += (greetings[formal] + ",\n\n")
    # part 2 : body
    for column in columnsList:
        template += (column + " : $" + column.split(" ")[0] + "\n\n")
    # part 3 : signature
    if signature:
        template += (signatures[formal] + ",\n" + author)
    return template