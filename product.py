products = [("Хлеб", 40, 5), ("Молоко", 60, 16), ("Яблоки", 100, 52)]
for product in products:
    name, price, kol = product
    print(f"Товар: {name}, Цена: {price}, Количество на складе: {kol}")
    
def find_product(products):
    print("Товары дешевле 80 рублей:")
    for name, price, kol in products:
        if price < 80:
            print(name)
            
def calc():
    for name, price, kol in products:
        result = price * kol
        print(f"{name} — всего на {result} рублей")
    
find_product(products)
calc()
