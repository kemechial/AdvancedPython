import smtplib
from email.mime.text import MIMEText

port = 587
smtp_server="smtp-relay.brevo.com"

login="7bee06003@smtp-brevo.com"
password="7avnXqOrLI68Qpfb"

sender_email="info@tester.com"
receiver_email="testerevran@gmail.com"

text="Hi, this is a test message."

message=MIMEText(text,"plain")
message["Subject"]="Test"
message["From"]=sender_email
message["To"]=receiver_email

with smtplib.SMTP(smtp_server,port) as server:
    server.starttls()
    server.login(login,password)
    server.sendmail(sender_email,receiver_email,message.as_string())

print("email sent.")