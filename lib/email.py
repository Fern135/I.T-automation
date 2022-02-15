import smtplib
import ssl
import os
from email.message import EmailMessage
from pathlib import Path  # Python 3.6 + only
from dotenv import load_dotenv, find_dotenv  # for using dotenv

load_dotenv(find_dotenv())

class Email:

    def __init__(self) -> None:
        self.message = EmailMessage()
        self.message["From"] = os.getenv("email")
        self.password        = os.getenv("email_password")


    # def setSender(self, sender_email) -> None:
    #     self.message["From"] = sender_email


    def setRecv(self,receiver_email) -> None:
        self.message["To"] = receiver_email


    def setSubject(self, subject) -> None:
        self.message["Subject"] = subject

    
    def attachDocument(self, document) -> None:
        self.message.add_alternative(document, subtype="html")
    

    def send(self) -> None:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = ssl.create_default_context()) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.receiver_email, self.message.as_string())

#region placeholder

# subject = "Email From Python"
# body = "This is a test email form Python!"
# sender_email = "coderacerlivestreamapp@gmail.com"
# receiver_email = "coderacerlivestreamapp@gmail.com"
# password = input("Enter a password: ")

# message = EmailMessage()
# message["From"] = sender_email
# message["To"] = receiver_email
# message["Subject"] = subject

# html = f"""
# <html>
#     <body>
#         <h1>{subject}</h1>
#         <p>{body}</p>
#     </body>
# </html>
# """

# message.add_alternative(html, subtype="html")
# context = ssl.create_default_context()


# with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message.as_string())

#endregion