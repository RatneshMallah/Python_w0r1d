import datetime


default_name = ["jusin", "john", "emilee", "jim", "Ron", "Sandra", "veronica", "Whitney"]
default_amounts = [234.34, 324.3423, 234, 324.43, 234 ,234.324, 234.234, 34534.345]

unf_message = """Hi {name}!

Thank you for the purchase on {date}.
We hope you are excited about using it. Just as a
reminder the purchase total was ${total}.
Have a great one!

Team $R.K.M.$ \n\n\n
"""

def make_messages(names, amounts):
	
	if len(names) == len(amounts):
		i = 0 
		today = datetime.date.today()
		text = '{today.month}/{today.day}/{today.year}'.format(today=today)
		for name in names:
			new_amount = "%.2f" %(amounts[i])
			new_msg = unf_message.format(
				name=name,
				date=text,
				total=new_amount 
				)
			i += 1
			print(new_msg)
		    


make_messages(default_name, default_amounts)

