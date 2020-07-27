products = {
    "Shirt": 100,
    "Pant": 200,
    "Tie": 50,
    "Belt": 50,
    "Jeans": 250
}

name = input("Enter product name:")
print(products[name])

if(name in products):
    print(products.get(name))
else:
    print("Product Not Found")