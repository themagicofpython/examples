x = input('Enter the first number: ')
y = input('Enter the second number: ')
try:
     print(int(x) / int(y))
except ZeroDivisionError:
     print("you can not divide by zero!")
except ValueError:
     print("Numbers can be divided only by numbers")
