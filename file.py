def add(outtxt):
    with open('outtxt', 'a') as f:
        f.write("hello.\n")
    
def readd(outtxt):
    try:
        with open('outtxt', 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print('файл не найден')
