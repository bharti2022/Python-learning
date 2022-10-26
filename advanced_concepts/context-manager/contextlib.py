# Python program for creating a
# context manager using @contextmanager
# decorator
from contextlib2 import contextmanager
from datetime import datetime
from time import sleep


@contextmanager
def timer():
    start = datetime.now()
    yield
    print(f"time taken {(datetime.now() -start).seconds}")

def timer_test():
    with timer():
        sleep(2)
        
if __name__ == '__main__':
    timer_test()
    
# @contextmanager
# def ContextManager():
	
# 	# Before yield as the enter method
# 	print("Enter method called")
# 	yield
	
# 	# After yield as the exit method
# 	print("Exit method called")

# with ContextManager() as manager:
# 	print('with statement block')