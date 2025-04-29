def add(outtxt):
    with open('outtxt', 'a') as f:
        f.write("hello.\n")
    
def readd(outtxt):
    try:
        with open('outtxt', 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print('файл не найден')

def factor(n):
    if n == 1:
        return 1
    return factor(n - 1) * n
f = open("fact", "w")
f.write(str(factor(11)))
f.close()
f = open("fact", 'r')
f.close
print(f.read())
    
