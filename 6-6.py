def getWeight(object):
   if isinstance(object, tuple):
      return object[1]
   elif isinstance(object, dict):
      return int(object['weight'])
   else:
      return get_weight_over_internet_method(object)

print(getWeight(('CW16348',20000)))
