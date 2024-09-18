class Dad:	
 	def work(self):
 	   print("I am too lazy to work")

class Mom:	
   def accept_blame(self):
       print("It is not my fault")

class Child(Dad,Mom):
	pass

Maria = Child()

print(hasattr(Maria,'work'))
print(hasattr(Maria,'dance'))
print(callable(getattr(Maria,'work',None)))
print(callable(getattr(Maria,'dance',None)))
