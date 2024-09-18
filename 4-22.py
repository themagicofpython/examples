import random

graph = {'A': ['B', 'C'], 'B':['C', 'D'], 
'C':['E'], 'D':['C'], 'E':['F'], 
'F':['E', 'B']}
pages = list(graph.keys())
visitations = {}
for page in pages:
	visitations[page] = 0
print(visitations)
current = random.choice(pages)
counter = 0
while counter<2000:
	counter += 1
	choice = random.randint(0, 6)
	if choice == 6:
		current = random.choice(pages)
	else:
		if current in graph and graph[current]:
			current = random.choice(graph[current])
	visitations[current] += 1
print(visitations)
