cw = 0
class AcmeContainer:
	def set_weight(self, weight):
		self.weight = weight
 	     
	def get_weight(self):
		return self.weight

class MegaContainer:
	def set_weight(self, weight):
		global cw
		cw = weight

	def get_weight(self):
		return cw
   	  
ac = AcmeContainer()
mc = MegaContainer()
ac.set_weight(4800)
mc.set_weight(5200)
print(ac.get_weight()) #prints 4800
print(mc.get_weight()) #prints 5200
mc2 = MegaContainer()
mc2.set_weight(6000)
print(mc2.get_weight()) #prints 6000
print(mc.get_weight()) #prints 6000
