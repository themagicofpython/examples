def make_error():
 	raise Exception("BAM!")
def call_faulty():
 	make_error()
call_faulty()
