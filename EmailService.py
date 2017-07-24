import smtplib

host = "smtp.gmail.com"
port = 587
username = "pythonworld2017@gmail.com"
password = "python75676"
from_email = username
to_list = ["rkm.sahajpur@gmail.com", "pythonworld2017@gmail.com"]

email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(from_email, to_list, "Hello There \nThis message for testing")
email_conn.quit()

from smtlib import SMTP, SMTPAuthenticationError, SMTPException

pass_wron = smtplib.SMTP(host, port)
pass_wron.ehlo()
pass_wron.starttls()
try:
	pass_wron.login(username, "pass_wrong")
	pass_wron.sendmail(from_email, to_list, "Hello There \nThis message for testing")
except SMTPAuthenticationError:
	print("Could not login")
except:
	print("an error ocured")

pass_wron.quit()
