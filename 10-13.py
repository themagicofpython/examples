import fileinput
for line in fileinput.input('somefile.txt'):
	print(line)
