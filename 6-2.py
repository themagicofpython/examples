class AcmeContainer:
 	def set_weight(self, weight):
 	     self.weight = weight

     def get_weight(self):
 		return self.weight

ac = AcmeContainer()
ac.set_weight(4800)
print(ac.get_weight())
