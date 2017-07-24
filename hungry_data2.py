import csv
import shutil
import datetime
from tempfile import NamedTemporaryFile


def get_length(file_path):
	with open("data.csv", "r") as csvfile:
		reader = csv.reader(csvfile)
		reader_list = list(reader)
		return len(reader_list)


def append_data(file_path, name, email):
	fieldnames = ["id", "name", "email"]
	next_id = get_length(file_path)
	with open(file_path, "a") as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		#writer.writeheader()
		writer.writerow({
			"id": next_id,
			"name": name,
			"email": email
			})


#append_data("data.csv", "justin", "hello@mail.com")
filename = "data.csv"
temp_file = NamedTemporaryFile(delete=False)

with open(filename, "rb") as csvfile, temp_file:
	print(temp_file.name)
	reader = csv.DictReader(csvfile)
	fieldnames = ["id", "name", "amount", "email", "sent", "date"]
	writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
	writer.writeheader()
	for row in reader:
		writer.writerow({
			"id": row["id"],
			"name": row["name"],
			"email": row["email"],
			"amount": "1222.22",
			"sent": "",
			"date": datetime.datetime.now()
			})

	shutil.move(temp_file.name, filename)