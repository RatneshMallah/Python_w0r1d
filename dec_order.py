num_ = input("Enter any number : ")
a_list = list(str(num_))
x = 0
for i in a_list:
	a_list[x] = int(i)
	x += 1
b_list = sorted(a_list, reverse=True)
num = map(str, b_list)
num = ''.join(num)
num = int(num)
print(num)