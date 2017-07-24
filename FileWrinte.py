file = open('a.txt', 'w')
file.write("Hello world gyz")

file = open('a.txt', 'r')
print(file.read())
file.close()