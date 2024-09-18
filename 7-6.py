class Fullname:
	def __len__(self):
		return 3
	def __getitem__(self, key):
		if key >= 0:
			if key == 0:
				return self.fname
			elif key == 1:
				return self.mname
			elif key == 2:
				return self.lname
			else:
				raise IndexError
		else:
			if key == -3:
				return self.fname
			elif key == -2:
				return self.mname
			elif key == -1:
				return self.lname
			else:
                raise IndexError

    def __setitem__(self, key, value):
        if key >= 0:
            if key == 0:
                self.fname = value
            elif key == 1:
                self.mname = value
            elif key == 2:
                self.lname = value
            else:
                raise IndexError
		else:
			if key == -3:
				self.fname = value
			elif key == -2:
				self.mname = value
			elif key == -1:
				self.lname = value
			else:
				raise IndexError

	def __init__(self,f,m,l):
		self.fname = f
		self.mname = m
		self.lname = l

name=Fullname("John", "Fitzgerald", "Kennedy")
print(name[-1])
for n in name:
	print(n)
