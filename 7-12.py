def fibonaci():
	a = 0
	b = 1
	tmp = 0
	yield a
	yield b
	while 1:
		tmp = a + b
		yield tmp
		a = b
		b = tmp

for i in fibonaci():
	print(i)
	if i>100:
		break

fib = fibonaci()
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
