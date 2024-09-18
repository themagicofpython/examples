import math
xnew = -2
x = 0
for i in range(100):
	x = xnew
	xnew = pow(x+10,0.25)
	if 	abs(xnew-x) < 0.001:
		break
print(x)
