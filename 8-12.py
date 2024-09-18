while 1:
	try:
		x = input('Enter the first number: ')
		y = input('Enter the second number: ')
		value = (int(x) / int(y))
		print('x/y is', value)
	except:
		print('Invalid input. Please try again.')
	else:
		break
