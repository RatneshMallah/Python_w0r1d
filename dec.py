word = raw_input("Type one santence : ")
word2 = word.split()
list_ = []
x = len(word2)
x = x-1
for item in word2:
	list_.append(word2[x])
	x -= 1
list_1 = ' '.join(str(z) for z in list_)
print(list_1)