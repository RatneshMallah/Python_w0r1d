def my_sum(my_num_list):
	total = 0
	for i in my_num_list:
		if isinstance(i, float) or isinstance(i, int):
			total += i
	return total


def addition(n1,n2):
	n3 = n1 + n2
	print(n1, "+", n2, "=", n3)


def substraction(n1,n2):
	n3 = n1 - n2
	print(n1, "-", n2, "=", n3)


def devision(n1,n2):
	n3 = n1 / n2
	print(n1, "/", n2, "=", n3)


def multiplication(n1,n2):
	n3 = n1 * n2
	print(n1, "*", n2, "=", n3)