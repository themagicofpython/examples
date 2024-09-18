products = []
s = input('Enter product name: ')
while s:
	products.append(s)
	s = input('Enter product name: ')
print(products)

names = ['Sulyo','Pulyo','Atanas','Az']
ages = ['19','21','24','30']
for i in range(len(names)):
	print(names[i],' is ',ages[i],' years old')
data = zip(names,ages)
for n,a in data:
	print(n,' is ',a,' years old')
