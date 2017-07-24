year = int(input("Enter The Year : "))
R  = '\033[31m' 
G  = '\033[32m'
W  = '\033[0m'  
O  = '\033[33m'
if (year%4 == 0) and (year%100 != 0 or year%400 == 0):
	print(''+G+'' "{0} is a leap Year".format(year))
	print(''+W+'')
else:
	print(''+R+'' "{0} is not a leap year".format(year))
	print(''+W+'')