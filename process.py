def process (text: str, flag: bool, number: float):
    for num in range(0, int(number)):
        kvad = num ** 2
        if num == 4:
            continue
        if num == 9:
            break
        if kvad > 50:
            print(f"Квадрат числа {number} больше 50")
        print(f"Квадрат числа {num} = {kvad}") 
process("sample text", True, 10.0)
process("hello", False, 52.0)
