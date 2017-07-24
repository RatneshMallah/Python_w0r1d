import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTPAuthenticationError


host = "smtp.gmail.com"
port = 587
username = "rkm.hacker@gmail.com"
password = "rkm75656"
from_email = username
to_list = ["rkm.hacker@gmail.com", "rahulsimplyblue9@gmail.com", "contactcyberflake@gmail.com", "shubham.chouksey96@gmail.com", "rkm.sahajpur@gmail.com", "shreyashah1920@gmail.com"]

try:
	email_conn = smtplib.SMTP(host, port)
	email_conn.ehlo()
	email_conn.starttls()
	email_conn.login(username, password)
	the_msg = MIMEMultipart("alternative")
	the_msg['Subject'] = "Hello there!"
	the_msg["From"] = from_email
	#the_msg["To"] = to_list[0]
	plain_text = "Testing the message"
	html_text = """\
	<html>
	  <head> <h1>Message for testint</h1></head>
	  <body>
	    <p>Hey!<br>
	      Testing this email <b>message</b>. Made by <a href='https://rkm01.blogspot.in'>Team $R.K.M.$</a>
	    </p>
	  </body>
	</html>
	"""
	part_1 = MIMEText(plain_text, 'plain')
	part_2 = MIMEText(html_text, 'html')
	the_msg.attach(part_1)
	the_msg.attach(part_2)
	email_conn.sendmail(from_email, to_list, the_msg.as_string())
	email_conn.quit()
except SMTPAuthenticationError:
	print("authrnticatin error")
	email_conn.quit()
except:
	print("sending message error")
	email_conn.quit()