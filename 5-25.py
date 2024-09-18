def outer():
	a = True 
	def inner():
		a = False
	
	print(a)

outer()
