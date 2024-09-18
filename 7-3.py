class BaseClass:
	def hello(self):
		print("Hello, I'm BaseClass.")
 
class Inherited(BaseClass):
	def hello(self):
		print("Hello, I'm Inherited.")
a.hello()
b.hello()
