class SomeClass:
	def __init__(self,lst=[]):
		self.lst = lst
	
	def add2lst(self,elem):
		self.lst.append(elem)
	
	def printlst(self):
		print(self.lst)

class Explained:
	lst = []
	def __init__(self,lst_arg):
		lst = lst_arg
	
	def add2lst(self,elem):
		self.lst.append(elem)
	
	def printlst(self):
		print(self.lst)	

class Working:
	def __init__(self):
		self.lst = []
	
	def add2lst(self,elem):
		self.lst.append(elem)
	
	def printlst(self):
		print(self.lst)	

a=SomeClass()
a.printlst()
a.add2lst("TEST")
a.printlst()

b=SomeClass()
b.printlst()
c=Working()
c.add2lst("TEST2")
c.printlst()

d=Working()
d.printlst()

e=Explained(['a','b'])
e.add2lst("TEST3")
e.printlst()

f=Explained([])
f.printlst()
