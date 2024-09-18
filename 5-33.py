import os
def get_file_list(path):
	for filename in os.listdir(path):
		print(path + "/" + filename)
		if os.path.isdir(path + "/" + filename):
			get_file_list(path + "/" + filename)
get_file_list('/home/user')
