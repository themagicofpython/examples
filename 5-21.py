def shadow_var():
   name = "Petrov"
   print(name)
   print(globals()['name'])

name = "Ivanov"
shadow_var()
