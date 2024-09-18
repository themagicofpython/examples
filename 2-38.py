num_list = [1,2,3,4,5]
for num in num_list:
	num = num * 2
print(num_list)
for index, num in enumerate(num_list):
	num_list[index] = num * 2
print(num_list)
