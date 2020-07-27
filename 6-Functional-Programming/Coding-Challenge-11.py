newlist = [30, 20, 40]
result = list(map(lambda x: x - (x - 10)/100, newlist))
print(result)