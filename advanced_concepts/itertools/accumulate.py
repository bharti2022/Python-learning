#finite iterators
from itertools import accumulate
import operator
print (list(accumulate(range(1, 5), operator.mul)))
"""Most of the iterators that you create with itertools
are not infinite. In this lesson, we will be studying 
the finite iterators of itertools"""
