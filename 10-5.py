f = open('news1.txt','r')
lines = f.readlines()
for l in lines:
 	print(l)
f.close()
