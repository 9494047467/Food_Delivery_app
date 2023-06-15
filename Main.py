# Food Delivery App

# Database of available restaurants
restaurants = {
    "1": {"name": "Restaurant A", "cuisine": "Italian", "rating": 4.5},
    "2": {"name": "Restaurant B", "cuisine": "Mexican", "rating": 3.8},
    "3": {"name": "Restaurant C", "cuisine": "Indian", "rating": 4.2}
}

# Database of menu items for each restaurant
menu = {
    "1": {"1": {"name": "Pizza", "price": 10.99}, "2": {"name": "Pasta", "price": 8.99}},
    "2": {"1": {"name": "Ice cream", "price": 6.99}, "2": {"name": "Lassi", "price": 7.99}},
    "3": {"1": {"name": "Biryani", "price": 9.99}, "2": {"name": "Curry", "price": 7.99}}
}

# Function to display available restaurants
def display_restaurants():
    print("Available Restaurants:")
    for key, value in restaurants.items():
        print(f"{key}. {value['name']} - Cuisine: {value['cuisine']}, Rating: {value['rating']}")

# Function to display the menu of a selected restaurant
def display_menu(restaurant_id):
    print("Menu:")
    for key, value in menu[restaurant_id].items():
        print(f"{key}. {value['name']} - ${value['price']}")

# Function to place an order
def place_order(restaurant_id, item_id):
    if restaurant_id in menu and item_id in menu[restaurant_id]:
        restaurant_name = restaurants[restaurant_id]['name']
        item_name = menu[restaurant_id][item_id]['name']
        item_price = menu[restaurant_id][item_id]['price']
        print(f"Order placed! You ordered {item_name} from {restaurant_name} for ${item_price}.")
    else:
        print("Invalid restaurant or item selection.")

# Main program loop
while True:
    print("Welcome to the Food Delivery App!")
    display_restaurants()

    # Get user input for restaurant selection
    restaurant_choice = input("Select a restaurant (enter the corresponding number): ")
    if restaurant_choice not in restaurants:
        print("Invalid restaurant selection. Please try again.")
        continue

    display_menu(restaurant_choice)

    # Get user input for menu item selection
    item_choice = input("Select a menu item (enter the corresponding number): ")
    if item_choice not in menu[restaurant_choice]:
        print("Invalid item selection. Please try again.")
        continue

    place_order(restaurant_choice, item_choice)

    # Ask if the user wants to place another order
    another_order = input("Would you like to place another order? (y/n): ")
    if another_order.lower() != "y":
        break

print("Thank you for using the Food Delivery App. Goodbye!")
