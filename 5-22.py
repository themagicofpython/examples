x = 1
y = 100

def change_global():
   global x
   x = x + 1
   y = 100
   
change_global()
print(x)
print(y)
