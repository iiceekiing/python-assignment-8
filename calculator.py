"""
TASK: Create a Calculator class.

Requirements:
1. The class should allow basic operations: add, subtract, multiply, divide.
2. Each operation should be a separate method.
3. Handle division by zero gracefully.
4. Allow both integers and floats.

Example Usage:
    calc = Calculator()
    print(calc.add(5, 3))        # 8
    print(calc.divide(10, 0))    # "Error: Division by zero"
"""
class Calculator:
    
    def __init__(self):
        pass
    def add(self, num1: int, num2: int) -> int:
        return num1 + num2
    
    def sub(self, num1: int, num2: int) -> int:
        return num1 - num2
    
    def mul(self, num1: int, num2: int) -> int:
        return num1 * num2
    
    def div(self, num1: int, num2: int) -> int:
        if num2 == 0:
            return f"ZeroDivisionError: cannot divide by 0"
        
        else:
            return num1 / num2
        
        
calc = Calculator()

print(calc.add(4, 6))
print()
print(calc.mul(4, 6))
print()
print(calc.div(4, -2))
print()
print(calc.sub(4, 6))