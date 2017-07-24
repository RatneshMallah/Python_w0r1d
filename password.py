i = 0
while i < 10:
	a = int(input("Enter the password : "))
	i += 1
	if (a == 98745):
		print("Congrats \nYou are logged")
		break
	elif (i == 5):
		while True:
			print("System is crashed")
			continue
	else:
		print("Password is wroong ")

