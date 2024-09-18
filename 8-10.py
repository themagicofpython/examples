x = input('Enter the first number: ')
y = input('Enter the second number: ')
try:
     print(repr(x)/repr(y))
except Exception as e:
     print(e)
