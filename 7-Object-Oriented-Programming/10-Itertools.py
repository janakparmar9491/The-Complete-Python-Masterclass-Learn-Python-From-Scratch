from itertools import count, accumulate, takewhile

for i in count(3):
    print(i)
    if i >= 20:
        break

numbers = list(accumulate(range(8)))
print(numbers)

numbers = list(takewhile(lambda x: x <= 10, numbers))
print(numbers)