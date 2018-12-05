import sys
import csv
import os, datetime

class Bank:
	BankNmae = "$R.K.M.$ Bank"

	def __init__(self,name):
		self.name = name
		self.balance = 0

	def Deposite(self,amount):
		self.balance = self.balance + amount
		print("\n{0} amount Deposite successfully\nCurrent Avialable Balance : {1}".format(amount,self.balance))
		dicto =  {
				"Name" : self.name, 
				"Deposite" : amount,
				"Total Amount" : self.balance, 
				"Date" : str(datetime.datetime.now())
			}
		self.writecsv(dicto)

	def Credit(self,amount):
		if self.balance<amount:
			print("insufficient Balance")
		else:
			self.balance = self.balance - amount
			print("\n{0} amount credit successfully\nCurrent Avialable Balance : {1}".format(amount,self.balance))
			dicto =  {
				"Name" : self.name, 
				"Credite" : amount,
				"Total Amount" : self.balance, 
				"Date" : str(datetime.datetime.now())
			}
			self.writecsv(dicto)

	def CheckBal(self):
		print("Current Balance : {bal}".format(bal=self.balance))

	@staticmethod
	def Options():
		print("\n          Choose Option\n-------------------------------")
		print("c - credit amount\nd - Deposite amount\ni - Check Avialable balance\ne - exit\no - Check Options\n")

	@staticmethod
	def writecsv(dicto):
		with open("data.csv", "a") as csvfile:
			fieldnames = ("Name", "Credite","Deposite","Total Amount", "Date")
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writerow(dicto)

	@staticmethod
	def readcsv():
		a = []
		with open("data.csv","r") as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				a.append(row)
		return a



print("\nWelcome to {bank}\n".format(bank=Bank.BankNmae))


def process(b):
	while True:
		inputo = input(": ")
		if inputo=='c':
			amo = int(input("Enter Ammount : "))
			b.Credit(amo)

		elif inputo=='d':
			amo1 = int(input("Enter Ammount : "))
			b.Deposite(amo1)

		elif inputo=='i':
			b.CheckBal()

		elif inputo=='e':
			print("\nThankyou For Banking\n")
			break

		elif inputo=='o':
			b.Options()

		else:
			print("You have Choose incorrect option")
			b.Options()




if 'data.csv' in os.listdir():
	pass
else:
	with open('data.csv','w') as csvfile:
		fieldnames = ("Name", "Credite","Deposite","Total Amount", "Date")
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		csvfile.close()


while True:
	name = input("Enter your name : ")
	data_dict = Bank.readcsv()
	flag = 0

	for i in data_dict:
		if i['Name']==str(name):
			flag+=1


	b = Bank(name)
	if flag==0:
		print("Your account does not exist\nWould you like to create account?")
		input1 = input(" y (yes), n (no): ")
		if input1 == 'y' or input1 == 'yes':
			try:
				dicto={
						"Name" : name, 
						"Date" : str(datetime.datetime.now())
					  }
				b.writecsv(dicto)
				print("\n{name} your accout created".format(name=name))
				b.Options()
				process(b)
			except:
				print("Account Creation Faild!")
				sys.exit()
		elif input1=='n' or input1=='no':
			pass
		else:
			print("you have Choose incorrect option")
			continue
	else:
		print("Welcome {name}\n".format(name=name))
		b.Options()
		process(b)





		

