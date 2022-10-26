# from contextlib2 import suppress

# with open('sample.txt') as fobj:
#     for line in fobj:
#         print(line)

from contextlib2 import suppress

with suppress(FileNotFoundError):
    with open('sample.txt') as fobj:
        for line in fobj:
            print(line)