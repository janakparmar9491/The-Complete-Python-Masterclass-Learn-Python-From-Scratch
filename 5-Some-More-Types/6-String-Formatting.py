numbers = [4, 5, 6]
string = "Numbers: {0}{1}{2}".format(numbers[0],numbers[1],numbers[2])
print(string)

numbers = [12, 12, 2016]
string = "Date: {0}/{1}/{2}".format(numbers[0],numbers[1],numbers[2])
print(string)

a = "{x}/{y}".format(x=100, y=200)
print(a)