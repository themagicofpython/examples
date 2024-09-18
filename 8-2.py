exceptions = []
temp = list([Exception])
while temp:
    exception = temp.pop()
    exceptions.append(exception)
    temp.extend(exception.__subclasses__())

for e in exceptions:
	print(e.__name__)
	print(e.__doc__)
	print("="*20)
