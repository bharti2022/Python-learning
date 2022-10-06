list1 = ['element1',2,'element2']
print(list1[2])
# using range()
num_seq = range(0,20)
print(type(num_seq))

num_list = list(num_seq)
print(num_list)

num_seq = range(3,20,3)
print(list(num_seq))

#sequential indexing
world_cup_winners = [[2006, "Italy"], [2010, "Spain"],
                     [2014, "Germany"], [2018, "France"]]
print(world_cup_winners[1])
print(world_cup_winners[1][1])  # Accessing 'Spain'
print(world_cup_winners[1][1][0])  # Accessing 'S'

#merge lists
part_A = [1, 2, 3, 4, 5]
part_B = [5, 6, 7, 8, 9, 10]
part_A.extend(part_B)
print(part_A)

#list comprehension

part_C = [n*3 for n in part_A]
print(part_C)

#list -comp with condition
part_D = [n*3 for n in part_A if n % 3 == 0]
print(part_D)

