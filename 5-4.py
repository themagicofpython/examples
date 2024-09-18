def bmi(weight, height):
   'Calculates Body mass index, weight in kg, height in meters'
   return weight/(height*height)
print(bmi(80,1.75))
print(bmi.__doc__)
