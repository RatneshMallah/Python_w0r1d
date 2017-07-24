def my_sum(my_num_list):
	total = 0
	for i in my_num_list:
		if isinstance(i, float) or isinstance(i, int):
			total += i
	return total