from contextlib2 import contextmanager
from datetime import datetime
from time import sleep
from contextlib2 import ExitStack
# filenames = "custom-context-manager2.py suppress-class-contextib.py redirect-stdout.py".split(" ")
# with ExitStack() as stack:
#     file_objects = [stack.enter_context(open(filename,'w')) for filename in filenames]
@contextmanager
def timer():
    start = datetime.now()
    yield
    print(f"time taken{(datetime.now() - start).seconds}")

# def timer_test():
#     with timer():
#         sleep(2)  

# if __name__ == '__main__':
#     timer_test()

@contextmanager
def print_blue():
    print("\033[34m")
    yield
    print("\033[39m")
    
def timer_test(time_to_sleep=2):
    sleep(2)
    with ExitStack() as stack:
        if time_to_sleep > 2:
           stack.enter_context(timer())
           stack.enter_context(print_blue())
        #    sleep(3)
           print("work done")
        # stack.enter_context(print_blue())
    # with print_blue:
    #     sleep(2)
    #     print("work done")    
    

if __name__ == '__main__':
    timer_test(3)
  