from easyMail import EasyMail
import pandas as pd 


print("\n***** Welcome to EasyMail *****\n")

# create an object of EasyMail class
mailerObject = EasyMail()

# read your data into a dataframe
data = pd.read_excel("demo.xlsx")

# list all columns in the excel sheet to be present in the email
columnsList = ["Roll Number", "Name", "Course", "Marks", "Grade"]

# create a template for your email using columnsList and templateGenerator
template = mailerObject.templateGenerator(columnsList=columnsList,formal=False,greeting=True, signature=True,author="Harshit Allumolu")
print(f"\nGenerated email body : {template}\n")

"""
    This part is coming soon!

    # extract the list of recepient email IDs
    emails = list(data["Email ID"])
    # check and correct any mistakes in email addresses
    emails = mailerObject.emailAddressCorrector(emails=emails)
    print("\nEmail Address corrections done (if any)!\n")
"""

# proceed to send an email
ret = mailerObject.sendEmail(emailId="YOUR EMAIL ID",password="YOUR PASSWORD",data=data[columnsList],emails=emails,subject="YOUR SUBJECT",body=template,author="HARSHIT ALLUMOLU")
if ret:
    print("\n***** Mails sent succesfully! *****\n")