"""
TASK: Create a ShoppingCart class.

Requirements:
1. Store cart items in a dictionary (item → quantity).
2. Provide a method to add items.
3. Provide a method to remove items.
4. Provide a method to clear the cart.
5. Provide a method to calculate total price (with price list).

Example Usage:
    prices = {"Shirt": 5000, "Shoes": 12000}
    cart = ShoppingCart(prices)
    cart.add_item("Shirt", 2)
    print(cart.calculate_total())  # 10000
    cart.remove_item("Shirt", 1)
    print(cart.calculate_total())  # 5000
"""

class ShoppingCart:
    def __init__(self, price_list):
        self.items = {}
        self.price_list = price_list

    def add_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity=1):
        if item in self.items:
            if quantity >= self.items[item]:
                del self.items[item]
            else:
                self.items[item] -= quantity

    def clear_cart(self):
        self.items.clear()

    def calculate_total(self):
        total = 0
        for item, quantity in self.items.items():
            if item in self.price_list:
                total += self.price_list[item] * quantity
        return total
    
# Example usage
prices = {"Shirt": 5000, "Shoes": 12000}
cart = ShoppingCart(prices)
cart.add_item("Shirt", 2)

print 
# print(cart.calculate_total())
# cart.remove_item("Shirt", 1)
# print(cart.calculate_total())  
# cart.add_item("Shoes", 1)
# print(cart.calculate_total()) 
# cart.clear_cart()
# print(cart.calculate_total())