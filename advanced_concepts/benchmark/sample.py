# importing the required module
from time import sleep
import timeit
def f1():
    for n in range(1,10):
        # print(n)
        pass

def f2():
    n=0
    sleep(10)
    while n < 11:
        # print(n)
        n=n+1

print(timeit.timeit(f1,number=10000))
print(timeit.timeit(f2,number=10000))
                
