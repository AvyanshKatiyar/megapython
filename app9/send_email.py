#a built in module 
# called email already exists in python

from email.mime.text import MIMEText
import smtplib
#what lecture was this in?

def send_email(email, height, avg, count_number):
    from_email="lerandomkidfrom8c@gmail.com"
    from_password="My name is khan"

    to_email=email
    subject="Height data"

    message= "Hey there, your height is <strong>%s</strong>. Looks like the average is %s out of %s beings."%(height, avg, count_number)
    msg=MIMEText(message, "html")
    msg["Subject"]=subject
    msg["To"]= to_email
    msg["From"]=from_email

    #https://www.youtube.com/watch?v=j7kMZD81hec smtp
    gmail=smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)