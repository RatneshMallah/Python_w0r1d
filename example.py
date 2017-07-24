#Python_w0r1d
import time
import sys
a = int(input("Enter a first value : "))
b = int(input("Enter a second value : "))
i = 0
j=10
bs = "\b\b\b\b\b\b"
while True:
	c = raw_input("what do you want to print odd/even : ")
	if c == "odd":
		while(a!=b):
			if(a%2!=0):
				print(a)
			a += 1
		break
	elif c == "even":
		while(a!=b):
			if(a%2==0):
				print(a)
			a += 1
		break
	else:
		print("input type is error '{c}'").format(c=c)
		if i==2:
			print "you take more time "
			"""while j!=0:
				print("wait {time_} sec.".format(time_=j)),
				j -= 1
				sys.stdout.write("\033[F")
				time.sleep(1),
				#print "\b\b\b\b\b"'\n'.join(),
				#time.sleep(1),
			"""
			for m in range(11):
				print("wait {time} sec.".format(time=j))
				sys.stdout.write("\033[F")
				j -= 1
				time.sleep(1)
	i += 1
 


