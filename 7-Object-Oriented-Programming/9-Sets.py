numbers = {1, 2, 3, 4, 5, 6}
print(5 in numbers)
numbers.add(7)
print(numbers)
numbers.remove(7)
print(numbers)

seta = {1, 2, 3, 4, 5}
setb = {4, 5, 6, 7, 8}
print(seta | setb) #union
print(seta & setb) #intersection
print(seta - setb)