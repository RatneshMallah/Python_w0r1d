items = ["Mic", "Phone", 23.34, 234.234, "Justin", "Bag", "Cliff Bars", 234]

print("items = ", items)

str_items = []
num_items = []

for i in items:
	if isinstance(i, float) or isinstance(i, int):
		num_items.append(i)
	elif isinstance(i, str):
		str_items.append(i)
	else:
		pass

print(str_items)

print(num_items)

def parse_lists(abc):
	str_list_items = []
 	num_list_items = []
	for i in abc:
		if isinstance(i, float) or isinstance(i, int):
			num_list_items.append(i)
		elif isinstance(i, str):
			str_list_items.append(i)
		else:
			pass
	return str_list_items, num_list_items

print("purse_list = ", parse_lists(items))



items3 = ["Mic", "Phone", 323.12, 234234.234, "justin", "bag", 3443]


def my_sum(my_num_list):
	total = 0
	for i in my_num_list:
		if isinstance(i, float) or isinstance(i, int):
			total += i
	return total

sum(items3)

my_sum(items3)
name = ["justin", "john", "EMILEE", "jim", "Ron", "aaa", "whitney"]
amounts = [4343.435,45435,45.34,543.5,345,54,3.324]

message = """Hi there!

Thank you for the purches on may 5th 2016.
We hope you are excited about using it. just as a
reminder the purcase total was $199.99.
Have a great one!

Team RKM
"""

