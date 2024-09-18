class BaseClass:
	def hello(self):
		print("Hello, I'm BaseClass.")

class Inherited(BaseClass):
	pass

a = BaseClass()
b = Inherited()
a.hello()
b.hello()
