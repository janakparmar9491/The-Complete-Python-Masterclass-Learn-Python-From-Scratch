def bmi(w, h):
    r = w / (h**2)
    return r

result = bmi(80, 1.75)
print(result)


def calculate_BMI(new_weight, new_height):
    new_bmi = new_weight / (pow(new_height, 2))
    return new_bmi


weight = float(input('Enter weight in Kgs'))
height = float(input('Enter height in meters'))
bmi = calculate_BMI(weight, height)
print(bmi)