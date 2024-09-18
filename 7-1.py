class Human:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def __str__(self):
		return f'My name is {self.name} and I am {self.age} years old.'

	def __repr__(self):
		return f'Human name:{self.name} \nHuman age: {self.age}'


h1 = Human('Ivon', 24)
print(f'{h1!s}')
print(f'{h1!r}')

print(f'{h1}')
