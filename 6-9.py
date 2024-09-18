class Human:
   def __init__(self,name):
      self.name = name
      
   def say_your_name(self):
      print("Hello, I am ",self.name)

class Zombie(Human):
   def say_your_name(self):
      print("Aaargh, ",self.name)

h1 = Human("Mariicho")
h1.say_your_name()
z1 = Zombie("Ivanka")
z1.say_your_name()
print(issubclass(Human,Human))
print(issubclass(Human,Zombie))
print(issubclass(Zombie,Human))
