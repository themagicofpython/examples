class Employee:
 	def __init__(self):
 		self.workhours = 8
 	def work(self):
 		print("I work", self.workhours," a day")

class Manager(Employee):
	def __init__(self):
            print("Go to work!")
a = Employee()
