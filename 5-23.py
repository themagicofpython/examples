def outer():
	def inner():
		print("This is the inner function")

	print("This is the outer function")
	inner()

outer()
