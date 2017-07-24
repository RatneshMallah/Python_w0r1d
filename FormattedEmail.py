import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587
username = "rkm.hacker@gmail.com"
password = "rkm75656"
from_email = username
to_list = ["rkm.hacker@gmail.com", "contactcyberflake@gmail.com"]


class MessageUser():
	user_details = []
	messages = []
	email_messages = []
	base_message = """Hi {name}!

Thank you for the purchase on {date}.
We hope you are excited about using it. Just as a 
reminder the purhase total was ${total}.
Have a great one!

Team $R.K.M.$
""" 
	def add_user(self, name, amount, email=None):
		name = name[0].upper() + name[1:].lower()
		amount = "%.2f" %(amount)
		detail = {"name":name , "amount":amount}
		today = datetime.date.today()
		date_text = "{today.day}/{today.month}/{today.year}".format(today=today)
		detail['date'] = date_text
		if email is not None:
			detail['email'] = email
		self.user_details.append(detail)
	def get_details(self):
		return self.user_details
	def make_messages(self):
		if len(self.user_details) > 0:
			for detail in self.get_details():
				name = detail['name']
				total = detail['amount']
				date = detail['date']
				message = self.base_message
				new_msg = message.format(
					name = name,
					total = total,
					date = date
					)
				user_email = detail.get("email")
				if user_email:
					user_data = {"email": user_email, "message": new_msg}
					self.email_messages.append(user_data)
				else:
					self.email_messages.append(new_msg)
			return self.messages
		return []
	def send_email(self):
		self.make_messages()
		if len(self.email_messages) > 0:
			for detail in self.email_messages:
				user_email = detail['email']
				user_message = detail['message']
				try:
					email_conn = smtplib.SMTP(host, port)
					email_conn.ehlo()
					email_conn.starttls()
					email_conn.login(username, password)
					the_msg = MIMEMultipart("alternative")
					the_msg['Subject'] = "Billing Update"
					the_msg["From"] = from_email
					the_msg["To"] = user_email
					part_1 = MIMEText(user_message, 'plain')
					the_msg.attach(part_1)
					email_conn.sendmail(from_email, [user_email], the_msg.as_string())
					email_conn.quit()
				except SMTPAuthenticationError:
					print("authrnticatin error")
			return True
		return False


obj = MessageUser()

obj.add_user("rkm", 234.234 , email='rahulsimplyblue9@gmail.com')
obj.add_user("hello", 23.32, email='contactcyberflake@gmail.com')
obj.add_user("john", 435.45, email='pythonworld2017@gmail.com')
obj.add_user("shubham", 34.43, "namdeoshubh@gmail.com")
obj.add_user("Riya", 34.45, "riyachourasiya1995@gmail.com")
obj.add_user("Shubham Chouksey", 5000, "shubham.chouksey96@gmail.com")
obj.get_details()
obj.send_email()
#print(obj.email_messages)