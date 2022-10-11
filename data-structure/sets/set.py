random_set = {"Educative", 1408, 3.142,
              (True, False)}
print(random_set)
print(len(random_set))  # Length of the set

exampl_set = set({"element1",121,1,3.3,(True,False)})

#   add element
exampl_set.add(333)

#delete existing
exampl_set.discard(121)

print(exampl_set)

#iterating a set
for num in exampl_set:
    print(num)
    

set_A = {1,2,3,4}
set_B = {1,'a','b','c','d'}
#union
print(set_A.union(set_B))
print(set_B.union(set_A))
#intersection
print(set_A.intersection(set_B))
#difference
print(set_A-set_B)
