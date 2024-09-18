class Employee:
	def __init__(self):
		self.workhours = 8

	def work(self):
		print("I work for ",self.workhours," a day")

class Manager(Employee):
	def __init__(self):
		super().__init__()

a = Employee()
b = Manager()
a.work()
b.work()
