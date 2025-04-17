def process (text: str, flag: bool, number: float):
    try:
        if text == "":
            raise valueError("строка пустая, напишите что-то")
    except:
        pass
    spisok = []
    for num in range(0, int(number)):
        kvad = num ** 2
        if num == 4:
            continue
        if num == 9:
            break
        if kvad > 50:
            print(f"Квадрат числа {number} больше 50")
        if kvad >= 20 and kvad <= 50:
            print(f"Квадрат числа {number} больше или равен 20 и меньше или равен 50")
        else:
            print(f"Квадрат числа {number} меньше 20")
        print(f"Квадрат числа {num} = {kvad}") 
        spisok.append(kvad)
        return spisok
process("sample text", True, 10.0)
process("hello", False, 52.0)
