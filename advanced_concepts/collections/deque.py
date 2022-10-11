from collections import deque
import string
d = deque(string.ascii_lowercase)
for letter in d:
    print(letter)
d.appendleft('test')
print (d)


d.rotate(1)
print (d)
