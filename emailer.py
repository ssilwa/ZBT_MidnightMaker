import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Send midnight emails after assignment
def send_email(server, toaddr, subject, body, fromaddr  = 'mitzbtmidnightmaker@gmail.com'):
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = subject
	msg.attach(MIMEText(body, 'plain'))
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)

