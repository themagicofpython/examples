class Factoriel:
	def __init__(self):
		self.n = 0
		self.f = 1

	def __next__(self):
		self.n = self.n+1
		self.f = self.n*self.f
		return self.f

	def __iter__(self):
		return self
 		
fact = Factoriel()
for f in fact:
	print(f)
	if f > 10000:
		break
