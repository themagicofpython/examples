def change_param(param):
   param[0] = "very important"
p = ["alabala","portakala"]
change_param(p[:])
print(p[0])
