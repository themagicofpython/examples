try:
     x = input('Enter the first number: ')
     y = input('Enter the second number: ')
     print(int(x) / int(y))
except ZeroDivisionError as e:
 	print("Stop dividing by zero!!!")
except:
 	print("something went wrong")
