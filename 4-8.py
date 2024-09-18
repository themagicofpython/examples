d = {'username':'filip','aliases':['phil','fil','fuf']}
d2 = d.copy()
d2['username'] = 'Mike'
d2['aliases'].remove('fuf')
print(d)
print(d2)
