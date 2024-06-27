import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = 'your_email@example.com'
receiver_email = 'receiver_email@example.com'
subject = 'Automated Email'
body = 'This is an automated email sent from a Python script.'

# Create the email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Send the email
with smtplib.SMTP('smtp.example.com', 587) as server:
    server.starttls()
    server.login(sender_email, 'your_password')
    server.sendmail(sender_email, receiver_email, msg.as_string())

print('Email sent successfully')
