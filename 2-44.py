def least_squares(l):
	xsquare = 0
	xsum = 0
	ysum = 0
	xsquare = 0
	xtimesy = 0
	for x, y in l:
		xsum += x
		ysum += y
		xsquare += x*x
		xtimesy += x*y
	b = (xsquare * ysum - xsum * xtimesy) / (xsquare * len(l) - xsum * xsum)
	m = (len(l) * xtimesy - xsum * ysum) / (xsquare * len(l) - xsum * xsum)
	return b, m

coordinates = [(8,3),(2,10),(11,3),(6,6),(5,8),(4,12),(12,1),(9,4),(6,9),(1,14)]
print(least_squares(coordinates))
