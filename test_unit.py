class matem:
    @staticmethod
    def factor(n):
        if n < 0:
            return None
        result = 1 
        for i in range(1, n + 1):
            result *= i 
        return result
    
    @staticmethod        
    def power(a, b):
        return a ** b
    
    @staticmethod        
    def sum_of_squares(n):
            return sum(i ** 2 for i in range(1, n + 1))
            
if __name__ == "__main__":
    num = 5
    print(f"факториал числа {num} равен {matem.factor(num)}")
    a = 2
    b = 3
    print(f"{a} в степени {b} равен {matem.power(a, b)}")
    n = 4
    print(f"сумма квадратов числа от 1 до {n} равна {matem.sum_of_squares(n)}")
