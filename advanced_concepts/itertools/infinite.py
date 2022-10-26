from itertools import count
from itertools import islice

for i in count(10):
    if i > 21: 
        break
    else:
        print(i)
print("-----------------")

for i in islice(count(10), 5):
    print(i)