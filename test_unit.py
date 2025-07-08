import unittest

class Matem:
    @staticmethod
    def factor(n):
        if n < 0:
            return None
        if n == 0:
            return 1
        result = 1 
        for i in range(1, n + 1):
            result *= i 
        return result
    
    @staticmethod        
    def power(a, b):
        return a ** b
    
    @staticmethod        
    def sum_of_squares(n):
        if n < 1:
            return 0
        return sum(i ** 2 for i in range(1, n + 1))
            
class TestMatem(unittest.TestCase):
    def test_factor(self):
        self.assertEqual(Matem.factor(5), 120)
        self.assertEqual(Matem.factor(0), 1)
        self.assertIsNone(Matem.factor(-3))
        
    def test_power(self):
        self.assertEqual(Matem.power(2, 3), 8) 
        self.assertEqual(Matem.power(5, 0), 1)
        
    def test_sum_of_squares(self):
        self.assertEqual(Matem.sum_of_squares(4), 30) 
        self.assertEqual(Matem.sum_of_squares(0), 0)
        
if __name__ == "__main__":
    unittest.main() 
