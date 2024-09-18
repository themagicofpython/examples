def f(x):
	return -x**2 + 8

def calc_integral_only_positive(a, b, f, n):
	delta = (b - a) / n
	s = 0.0
	for i in range(n):
		c = delta * f(a + (i) * delta)
		if c > 0:
			s += c
	return s
print(calc_integral_only_positive(-4, 4, f, 1000))
