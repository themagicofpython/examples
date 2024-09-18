def callback():
	print("callback")

def accept(function):
	print("running function")
	function()
	print("end function")	

accept(callback)
