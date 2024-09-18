class CounterList(list):
     def __init__(self, *args):
          super(CounterList, self).__init__(*args)
          self.counter = 0
          
     def __getitem__(self, index):
          self.counter += 1
          return super(CounterList, self).__getitem__(index)

cl = CounterList(range(10))
print(cl)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cl.reverse()
print(cl)
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
del cl[3:6]
print(cl)
[9, 8, 7, 3, 2, 1, 0]
print(cl.counter)
cl[4] + cl[2]
print(cl.counter)
