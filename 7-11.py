def fibonaci(n):
	a = 0
	b = 1
	tmp = 0
	for i in range(1,n):
		tmp = a + b
		a = b
		b = tmp
	return b
	
for i in range(1,10):
	print(fibonaci(i))
