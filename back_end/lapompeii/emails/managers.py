from django.db import models
from django.db import transaction

from emails.models import Emails
from emails.serializers import EmailsSerializer
from datetime import datetime, timedelta

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import re

class EmailsManager(models.Manager):

    @staticmethod
    def SendVerificationEmail(name, email, phone, comment):
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = # Enter your address
        receiver_email = # Enter receiver address
        password = # Enter sender_email password
        message = MIMEMultipart("alternative")
        message["Subject"] = "New Message from: " + str(name)
        message["From"] = sender_email
        message["To"] = receiver_email
        # Create the plain-text and HTML version of your message
        
        text = """\
        New Message from:
        Name: """ + name + """"
        Email: """ + email + """"
        Phone: """ + str(phone) + """"
        Message: """ + str(comment)
        
        html = """\
        <html>
          <body>
            <p><h4>New Message from:</h4>
               <b>Name:</b> """ + name + """<br>
               <b>Email:</b> """ + email + """<br>
               <b>Phone:</b> """ + str(phone) + """<br>
               <b>Message:</b><br><p> """ + str(comment) + """</p><br>  
            </p>
          </body>
        </html>
        """         
    
        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        
        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)
        
        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

    @staticmethod
    def ReturnEmails(serialize=True):
        """
        Retrieves all emails in DB.

        """
        list = Emails.objects.all()
        if serialize:
            serializer = EmailsSerializer(list, many=True)
            return serializer.data
        else:
            return list

    @staticmethod
    def Create(createData):
        """
        Creates an email with specified data.

        """
        print ('create')
        if 'label' in createData:
            createData['label'] = re.sub('<[^<]+?>', '', createData['label'])
                
        serializer = EmailsSerializer(None, data=createData)
        if serializer.is_valid():
            created = EmailsSerializer(serializer.save())
            EmailsManager.SendVerificationEmail(createData['name'], createData['email'], createData['phone'], createData['comment'])
            return (True, created.data,)
        else:
            return (False, serializer.errors,)

    @staticmethod
    def Find(id, serialize=True):
        """
        Retrieves an email by its ID. 

        """
        try:
            a = Emails.objects.get(id=id)
        except:
            return (False, None,)

        if serialize:
            serializer = EmailsSerializer(a)
            category = serializer.data
            return (True, email,)
        else:
            return (True, a,)

    @staticmethod
    def Delete(id):
        """
        Deletes an email specified by its ID.

        """
        try:
            a = Emails.objects.get(id=id)
        except:
            return False
        if a.delete():
            return True
        else:
            return False

    @staticmethod
    def Update(id, updateData):
        """
        Updates an email with specified data.

        """
        print('update')
        if 'label' in updateData:
            updateData['label'] = re.sub('<[^<]+?>', '', updateData['label'])        
        a = None
        try:
            a = Emails.objects.get(id=id)
        except Exception as e: print(e)
            
        serializer = EmailsSerializer(a, data=updateData)
        if serializer.is_valid():
            updated = EmailsSerializer(serializer.save())
            return (True, updated.data,)
        else:
            return (False, serializer.errors,)    