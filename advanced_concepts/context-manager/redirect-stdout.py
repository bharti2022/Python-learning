from contextlib2 import redirect_stdout

with open('text.txt', 'w') as f:
    with redirect_stdout(f):
        print("hello this is to be stored in file")       