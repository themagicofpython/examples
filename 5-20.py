def shadow_var():
   name = "Petrov"
   #Here we have a problem if we want to access the global "name"
name = "Ivanov"
shadow_var()
