n = None
while n is None:
	try:
		s = raw_input("Enter a password : ")
		n = int(s)
		if n == 12345:
			print "You are logged!"
			break
		else:
			print "Password is wrong"
			n = None

	except ValueError:
		b = [ord(c) for c in s]
		a = 0
		for i in b:
			if i>=65 and i<=90 or i>=97 and i<=122:
				a += 1
				if a == 1:
					print("Alphabets not allowed")
			else:
				a += 1
				if a == 1:
					print("Spacial Symball not allow")
					
		


