import datetime
i = 0
while i < 10:
	now = datetime.datetime.now()
	a = str(raw_input("Enter the password : "))
	i += 1
	if (a == now.strftime('8%m4%H2%d1%Y')):
		print("Congrats \nYou are logged")
		break
	elif (i == 5):
		while True:
			print("System is crashed")
			continue
	else:
		print("Password is wroong ")


