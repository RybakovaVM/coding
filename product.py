products = [("Хлеб", 40), ("Молоко", 60), ("Яблоки", 100)]
for product in products:
    name, price = product
    print(f"Товар: {name}, Цена: {price}")
    
def find_product(products):
    print("Товары дешевле 80 рублей:")
    for name, price in products:
        if price < 80:
            print(name)
    
find_product(products)
