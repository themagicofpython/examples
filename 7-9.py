class car:
	def __init__(self,brand,model):
		self._brand = brand
		self._model = model

	@property
	def brand(self):
		return self._brand

	@brand.setter
	def brand(self, brand):
		self._brand = brand

	@property
	def model(self):
		return self._model

	@model.setter
	def model(self,model):
		self._model = model

	@brand.deleter
	def brand(self):
		self.brand = None


fe = car('Ford','Escort')
print(fe.brand,fe.model)
fe.model = 'Fiesta'
del fe.brand
print(fe.brand,fe.model)
