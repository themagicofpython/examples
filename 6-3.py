class Zombie:
   members = 0
   def __init__(self,name):
      self.name = name
      
   def say_your_name(self):
      print("Aaargh, ",self.name)

   def summon(self):
      Zombie.members += 1

z1 = Zombie("Mariicho")
z1.summon()
print(Zombie.members)
z2 = Zombie("Ivanka")
z2.summon()
print(Zombie.members)

z1.say_your_name()
z2.say_your_name()
