"""
TASK: Create a RestaurantOrder class.

Requirements:
1. Store orders in a dictionary (item → quantity).
2. Provide a method to add items to the order.
3. Provide a method to remove items from the order.
4. Provide a method to calculate the total bill (use a price list dictionary).
5. Provide a method to show the current order.

Example Usage:
    prices = {"Pizza": 2000, "Burger": 1500, "Drink": 500}
    order = RestaurantOrder(prices)
    order.add_item("Pizza", 2)
    order.add_item("Drink", 3)
    print(order.calculate_total())  # 5500
"""
