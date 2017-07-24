import datetime


class MessageUser():
	user_details = []
	base_message = """\nHi {name}!

Thank you for the purchase on {date}.
We hope you are excited about using it. Just as a
reminder the purchase total was ${total}.
Have a great one!

Team $R.K.M.$ \n

"""
	def add_user(self, name, amount):
		name = name[0].upper() + name[1:].lower()
		amount = "%.2f" %(amount)
		detail = {"name": name, "amount": amount}
		today = datetime.date.today()
		date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
		detail['date'] = date_text
		self.user_details.append(detail)
	def get_details(self):
		return self.user_details
	def make_messages(self):
		if len(self.user_details) > 0:
			for detail in self.get_details():
				name = detail["name"]
				amount = detail["amount"]
				date = detail["date"]
				message = self.base_message
				new_msg = message.format(
					name = name,
					date = date,
					total = amount	
				)
				print(new_msg)
		return []

"""
obj = MessageUser()
obj.add_user("justin", 123.24)
obj.add_user("john", 545.464)
obj.add_user("rkm", 78.25)
obj.add_user("shubham", 457.5)
obj.get_details()
obj.make_messages()
"""






