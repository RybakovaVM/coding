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
        
price = []
def search():
    global price
    for product in products:
       result = int(product[1]) * int(product[2])
       price.append(result)
       price.sort()
       price.reverse()
       print(price)
       for product in products:
           if (int(product[1]) * int(product[2])) == price[0]:
            name = product[0]
            if (int(product[1]) * int(product[2])) == price[0]:
                print(f"Самая большая цена у товара {name} - {price[0]}")   

find_product(products)
calc()
search()
