x = input('Enter the first number: ')
y = input('Enter the second number: ')
try:
     print(int(x) / int(y))
except (ZeroDivisionError,ValueError) as e:
     print("Error:", e)
