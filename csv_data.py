import csv
import shutil
import datetime
from tempfile import NamedTemporaryFile

def read_data(user_id=None,email=None):
	with open("data.csv", "r") as csvfile:
		reader = csv.DictReader(csvfile)
		unknown_user_id = None
		unknown_user_email = None
		for row in reader:
			if user_id is not None:
				if int(user_id) == int(row.get("id")):
					return row
				else:
					unknown_user_id = user_id
			if email is not None:
				if str(email) == str(row.get("email")):
					return row
				else:
					unknown_user_email = email
		if unknown_user_id is not None:
			return "User id {user_id} is not found".format(user_id=unknown_user_id)
		if unknown_user_email is not None:
			return "User email {user_email} is not found".format(user_email=unknown_user_email)


def get_length(file_path):
	with open("data.csv", "r") as csvfile:
		reader = csv.reader(csvfile)
		reader_list = list(reader)
		return len(reader_list)


def append_data(file_path, name, email, amount):
	fieldnames = ["id", "name", "email", "amount", "sent", "date"]
	next_id = get_length(file_path)
	with open(file_path, "a") as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		#writer.writeheader()
		writer.writerow({
			"id": next_id,
			"name": name,
			"email": email,
			"amount": amount,
			"sent": "",
			"date": datetime.datetime.now()
			})


#append_data("data.csv", "justin", "hello@mail.com",123.22)
def edit_data(edit_id=None,email=None, amount=None, sent=None):
	file_name = "data.csv"
	temp_file = NamedTemporaryFile(delete=False)

	with open (file_name, "rb") as csvfile, temp_file:
		reader = csv.DictReader(csvfile)
		fieldnames = ["id","name","email","amount","sent","date"]
		writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
		writer.writeheader()
		for row in reader:
			#print(row)
			if edit_id is not None:
				if int(row['id']) == int(edit_id):
					row['amount'] = amount
					row['sent'] = sent
			elif email is not None and edit_id is None:
				if str(row['email']) == str(email):
					row['amount'] = amount
					row['sent'] = sent
			else:
				pass
			writer.writerow(row)

	print(temp_file.name)
	shutil.move(temp_file.name,file_name)