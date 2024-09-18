from copy import deepcopy
d = {'username':'filip','aliases':['phil','fil','fuf']}
d2 = d.copy()
d3 = deepcopy(d)
d['aliases'].append('Felipe')
print(d2)
print(d3)
