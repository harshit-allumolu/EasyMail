"""

Author : Harshit Allumolu <allumoluharshit@gmail.com>

Functionality : To send personal emails using smtplib-python and gmail client

Idea : The goal is to automate sending same email to multiple users with user-specific data.

Let's dive into the code for more details!

"""

# import required modules
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
from .generateTemplate import generateTemplate
from .correctAddress import correctAddress
import re
from string import Template

class EasyMail():
    """
        Class name : EasyMail
    """
    def __init__(self):
        pass



    def templateGenerator(self, columnsList : list, formal : bool = True, greeting : bool = True, signature : bool = False, author : str = None) -> str:
        """    
            Function name : templateGenerator

            Arguments : 
                -- columnsList (list type) : A list containing all column names in the excel sheet. Mention only those columns which are needed in the template.
                -- formal (bool type) : A boolean flag for formal/informal type switch. (default = True)
                -- greeting (bool type) : A boolean flag to include or not the greeting line in the email template. (default = True)
                -- signature (bool type) : A boolean flag to indicate if bottom section of the email with your name is required or not. (default = False)
                -- author (str type) : The name of the person who is writing this email. This must be given if signature is True.

            Return :
                -- A template which is of type str
        """
        return generateTemplate(columnsList = columnsList, formal = formal, greeting = greeting, signature = signature, author = author)



    def emailAddressCorrector(self, emails : list) -> list:
        """
            Function name : emailAddressCorrector

            Arguments :
                -- emails : A list of all email IDs in the excel sheet
            
            Return :
                -- A list of email IDs with corrected domain names
        """
        return correctAddress(emails = emails)



    def stringToHTML(self, template : str):
        template = f"<html>{template}</html>"
        template = re.sub("\n","<br>",template)
        # TODO : make every editable field bold
        return Template(template)



    def sendEmail(self, emailId : str, password : str, data : pd.DataFrame, emails : list, subject : str, body : str, author : str, uniqueAttachmentFiles : list = None, commonAttachmentFiles : list = None) -> bool:
        """
            Function name : sendEmail

            Arguments :
                -- emailId (str type) : EMAIL ID (gmail)
                -- password (str type) : gmail password
                -- data (pandas DataFrame) : A dataframe of excel sheet only with required columns
                -- emails (list type) : A list of all email IDs
                -- body (str type) : email template
                -- uniqueAttachmentFiles (list type) : A list of paths of all unique attachments
                -- commonAttachmentFiles (str type) : A list of paths to a common attachments file for all

            Return :
                -- return True if everything is fine, else False
        """
        try:
            session = smtplib.SMTP(host="smtp.gmail.com",port=587)
            session.starttls()
            session.login(user=emailId, password=password)
            columnsList = list(data.columns)
            for i in range(len(data)):
                message = MIMEMultipart()
                message["From"] = author
                message["To"] = emails[i]
                message["Subject"] = subject
                messageTemplate = self.stringToHTML(body)
                subs = dict()
                for j in range(len(columnsList)):
                    subs[columnsList[j].split(" ")[0]] = data.iloc[i,j]
                messageBody = messageTemplate.substitute(subs)
                message.attach(MIMEText(messageBody,"html"))
                if commonAttachmentFiles is not None:
                    for attachmentFile in commonAttachmentFiles:
                        attachment = open(attachmentFile, "rb")
                        payload = MIMEBase('application', 'octet-stream')
                        payload.set_payload((attachment).read())
                        encoders.encode_base64(payload)
                        payload.add_header('Content-Disposition', "attachment; filename= %s" % attachmentFile)
                        message.attach(payload)
                if uniqueAttachmentFiles is not None:
                    if len(uniqueAttachmentFiles) == len(data):
                        attachment = open(uniqueAttachmentFiles[i], "rb")
                        payload = MIMEBase('application', 'octet-stream')
                        payload.set_payload((attachment).read())
                        encoders.encode_base64(payload)
                        payload.add_header('Content-Disposition', "attachment; filename= %s" % uniqueAttachmentFiles[i])
                        message.attach(payload)
                session.send_message(message)
                del message
            session.quit()
            return True
        except:
            print("Sorry! There is some error which caused the process to stop. Please make sure you have followed all the guidelines correctly")
            return False