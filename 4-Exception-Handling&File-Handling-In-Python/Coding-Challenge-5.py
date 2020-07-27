def cal(a, b):
    try:
        return (a/b)
    except ZeroDivisionError:
        error = "There is a divide by zero error"
        return error

result = cal(15, 0)
print(result)
