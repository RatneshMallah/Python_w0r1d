import datetime
a = datetime.datetime.today().weekday()
today = datetime.date.today()
text = '{today.day}/{today.month}/{today.year}'.format(today=today)
if a == 0:
	print("It's Monday.")
	print(text)
elif a == 1:
	print("It's Tuesday.")
	print(text)
elif a == 2:
	print("It's Wednesday")
	print(text)
elif a == 3:
	print("It's Thursday.")
	print(text)
elif a == 4:
	print("It's Friday.")
	print(text)
elif a == 5:
	print("It's Saturday.")
	print(text)
elif a == 6:
	print("It's Sunday.")
	print(text)

#M@d3 by $R.K.M.$
