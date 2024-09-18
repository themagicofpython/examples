numbers=[72, 101, 108, 108, 111, 44, 32, 119, 111, 114,
108, 100, 33]
n2 = filter(lambda n: n % 2 == 0, numbers)
for element in n2:
    print(element)
