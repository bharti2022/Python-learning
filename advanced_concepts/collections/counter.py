from collections import Counter
print (Counter('superfluous'))

counter = Counter('superfluous')
print (counter['u'])

#elements()
Counter('superfluous')
counter = Counter('superfluous')
print (list(counter.elements()))

#most_common()
Counter('superfluous')
counter = Counter('superfluous')
print( counter.most_common(2))


#subtract
counter_one = Counter('superfluous')
print (counter_one)
counter_two = Counter('super')
print(counter_one.subtract(counter_two))
print (counter_one)
