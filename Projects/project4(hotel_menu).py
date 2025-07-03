# HOTEL MENU

class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class HotelMenu:
    def __init__(self):
        self.categories = {
            "Starters": [],
            "Soup": [],
            "Main Course": [],
            "Side Dishes": [],
            "Sweets": [],
            "Ice Cream": []
        }

    def add_dish(self, category, dish):
        if category in self.categories:
            self.categories[category].append(dish)
        else:
            print(f"Invalid category: {category}. Please choose from: {', '.join(self.categories.keys())}")

    def display_menu(self):
        print("\033[1mHotel Menu:\033[0m")
        for category, dishes in self.categories.items():
            print(f"\n\033[1m{category}:\033[0m")
            for dish in dishes:
                print(f"{dish.name}: ${dish.price:.2f}")

    def take_order(self):
        order = []
        while True:
            self.display_menu()
            category = input("Enter the category of the dish you want to order (or 'done' to finish): ").strip()
            if category.lower() == 'done':
                break
            if category in self.categories:
                dish_name = input("Enter the name of the dish: ").strip()
                dish = next((d for d in self.categories[category] if d.name.strip() == dish_name), None)
                if dish:
                    quantity = int(input(f"How many {dish_name.strip()} would you like to order? "))
                    order.append((dish, quantity))
                else:
                    print(f"Dish '{dish_name}' not found in category '{category}'.")
            else:
                print(f"Invalid category: {category}. Please choose from: {', '.join(self.categories.keys())}")
        return order

    def ask_for_sweets(self, order):
        while True:
            sweet_order = input("Would you like to order any sweet dishes? (yes/no): ").strip().lower()
            if sweet_order == 'yes':
                self.display_menu()
                category = "Sweets"
                dish_name = input("Enter the name of the sweet dish: ").strip()
                dish = next((d for d in self.categories[category] if d.name.strip() == dish_name), None)
                if dish:
                    quantity = int(input(f"How many {dish_name.strip()} would you like to order? "))
                    order.append((dish, quantity))
                else:
                    print(f"Dish '{dish_name}' not found in category '{category}'.")
            elif sweet_order == 'no':
                break
            else:
                print("Please enter 'yes' or 'no'.")
        return order

    def generate_bill(self, order):
        total = 0
        print("\n\033[1mBill:\033[0m")
        for dish, quantity in order:
            cost = dish.price * quantity
            total += cost
            print(f"{dish.name.strip()} x {quantity}: ${cost:.2f}")
        print(f"\nTotal: ${total:.2f}")

if __name__ == "__main__":
    menu = HotelMenu()

    # Adding dishes
    menu.add_dish("Starters", Dish("Garlic Bread", 40))
    menu.add_dish("Starters", Dish("Vegetable Samosa", 30))
    menu.add_dish("Starters", Dish("Masala Papad", 20))
    menu.add_dish("Starters", Dish("Chilly Manchurian", 60))
    menu.add_dish("Starters", Dish("Paneer Chilly", 120))

    menu.add_dish("Soup", Dish("Tomato Soup", 50))
    menu.add_dish("Soup", Dish("Manchow Soup", 50))
    menu.add_dish("Soup", Dish("Palak Soup", 50))
    menu.add_dish("Soup", Dish("Sweet Corn Soup", 50))
    menu.add_dish("Soup", Dish("Chicken Spicy Soup", 80))

    menu.add_dish("Main Course", Dish("Paneer Tikka Masala", 160))
    menu.add_dish("Main Course", Dish("Chicken Biryani (half)", 180))
    menu.add_dish("Main Course", Dish("Mix Veg", 120))
    menu.add_dish("Main Course", Dish("Veg Punjabi", 150))
    menu.add_dish("Main Course", Dish("Paneer Maratha", 180))
    menu.add_dish("Main Course", Dish("Paneer Tandoor Biryani", 240))
    menu.add_dish("Main Course", Dish("Chicken Zankka", 159))
    menu.add_dish("Main Course", Dish("Chicken Maratha", 189))
    menu.add_dish("Main Course", Dish("Chicken Tandoor Masala", 199))
    menu.add_dish("Main Course", Dish("Chicken Tandoor Biryani (half)", 259))

    menu.add_dish("Side Dishes", Dish("Sprouts Salad", 80))
    menu.add_dish("Side Dishes", Dish("Veg Salad", 50))
    menu.add_dish("Side Dishes", Dish("Roasted Papad", 50))

    menu.add_dish("Sweets", Dish("Gulabjam", 50))
    menu.add_dish("Sweets", Dish("Jilebi", 50))
    menu.add_dish("Sweets", Dish("Rabaddi", 50))

    menu.add_dish("Ice Cream", Dish("Cornato", 50))
    menu.add_dish("Ice Cream", Dish("Dark Chocolate", 150))
    menu.add_dish("Ice Cream", Dish("London Berry", 250))
    menu.add_dish("Ice Cream", Dish("Vanilla Scoop", 80))

    # Display the complete menu
    menu.display_menu()

    # Take order and generate bill
    order = menu.take_order()
    order = menu.ask_for_sweets(order)
    menu.generate_bill(order)
