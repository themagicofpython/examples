class car:
	def __init__(self,b,m):
		self.brand = b
		self.model = m

	def get_brand(self):
		return self.brand

	def set_brand(self,b):
		self.brand = b

	def set_model(self,m):
		self.model = m

	def get_model(self):
		return self.model

	def del_brand(self):
		self.brand = None

	Model = property(get_model,set_model)
	Brand = property(get_brand, set_brand, del_brand)

fe = car('Ford','Escort')
print(fe.brand,fe.model)
fe.Model = 'Fiesta'
print(fe.Brand,fe.Model)
del fe.Brand
