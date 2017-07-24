import datetime
z = 0
while z < 10:
	z += 1
	try:
		now = datetime.datetime.now()
		s = raw_input("Enter the password : ")
		q = int(s)
		if (q == now.strftime('8%m4%H2%d1%Y')):
			print("Congrats \nYou are logged")
			break
		elif (z == 5):
			while True:
				print("System is crashed")
		else:
			print("Password is wrong ")

	except ValueError:
		b = [ord(c) for c in s]
		a = 0
		if (z == 5):
			while True:
				print("System is crashed")
		else:
			for i in b:
				if i>=65 and i<=90 or i>=97 and i<=122:
					a += 1
					if a == 1:
						print("Alphabets not allowed")
				else:
					a += 1
					if a == 1:
						print("Spacial Symball not allow")


