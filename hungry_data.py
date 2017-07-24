import csv  
		

def get_length(file_path):
	with open("data.csv", "r") as csvfile:
		reader = csv.reader(csvfile)
		reader_list = list(reader)
		return len(reader_list)


def append_data(file_path, name, email):
	fieldnames = ('id', 'name', 'email')
	#the number of rows
	next_id = get_length(file_path)
	with open(file_path, "a") as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		if next_id == 0:
			writer.writeheader()
			writer.writerow({
				"id": 1,
				"name": name,
				"email": email,
				})
		else:
			writer.writerow({
				"id": next_id,
				"name": name,
				"email": email,
				})
			print(writer.writeheader())



while True:
	name_input = raw_input("name : ")
	if name_input == "exit":
		break
	else:
		name = name_input
		name = name[0].upper() + name[1:].lower()
	email_input = raw_input("email : ")
	if email_input == "exit":
		break
	else:
		email = email_input
	print("\n")
	append_data("data.csv", name, email)
