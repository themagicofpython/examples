containers = [
{'cid':10, 'weight': 10000, 'ctype' : 'car'},
{'cid':11, 'weight': 9800, 'ctype': 'construction'},
{'cid':12, 'weight': 11000, 'ctype' : 'car'},
{'cid':13, 'weight': 10500, 'ctype' : 'construction'},
{'cid':14, 'weight': 10200, 'ctype' : 'car'},
{'cid':15, 'weight': 9600, 'ctype' :'construction'}
]

lightest = functools.reduce(lambda tweight, weight:tweight+weight, map(lambda element: element['weight'], filter(lambda element:element['ctype'] == 'car', containers)))
print(lightest)
