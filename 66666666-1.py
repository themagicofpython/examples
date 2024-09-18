class SimpleCalc:	
	def add(self,*a):
		result = 0
		for num in a:
			result += num			
		return result

	def multiply(self,*a):
		result = 1
		for num in a:
			result *= num			
		return result

calc = SimpleCalc()
print(calc.add(1,2,3,100)) #prints 106
print(calc.multiply(1,2,3,4)) #prints 24
