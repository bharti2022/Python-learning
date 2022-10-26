print(any([True,False,True,False]))

#enumerate
my_string = 'abcdefgaaa'
for pos, letter in enumerate(my_string):
    print (pos, letter)

#0 a
#1 b
#2 c
#3 d
#4 e
#5 f
#6 g

#eval
var=10
source = 'var*2'
print(source)
print(eval(source))

#filter and map

my_list = [1, 2, 3, 10, 11, 12]
for item in filter(lambda x:x<10, my_list):
    print(item)

print("-----------------------------")
#1
#2
#3
#map()
for item in map(lambda x:x*2, my_list):
    print(item)
print("-----------zip-------------")
#zip
"""The zip built-in takes a series of iterables 
and aggregates the elements from each of them."""
keys = ['x', 'y', 'z']
values = [5, 6, 7, 8]
# print (zip(keys, values))

print (list(zip(keys, values)))