import random

def greet():
    responses=("Hello, how are u:" , "welcome in our shop:")
    return random.choice(responses)

def your_order():
    responses=("What is your order? ", "May i take your order:")
    return random.choice(responses)

def ask_for_size():
    responses = ["What size would you like? (Small, Medium, Large)", "Would you like a small, medium, or large?"]
    return random.choice(responses)

def confirm_order():
    responses = ["Great choice! Your order will be ready shortly.", "Thank you for your order!"]
    return random.choice(responses)

def handle_menu_item(item):
    responses = {
        "coffee": "Sure, what type of coffee would you like? (Espresso, Latte, Cappuccino, etc.)",
        "tea": "We have a variety of teas available. What kind would you like?",
        "pastry": "We have a selection of pastries. Which one would you like?",
        "sandwich": "We offer a variety of sandwiches. What kind are you interested in?"
    }
    return responses.get(item, "I'm sorry, we don't have that item.")

def handle_size(size):
    sizes = ["small", "medium", "large"]
    if size.lower() in sizes:
        return f"Your {size.lower()} {current_order} will be ready shortly."
    else:
        return "I'm sorry, we don't offer that size."
    
def chat():
    print(greet())
    print(your_order())

    order = input().lower()
    if order in ["coffee", "tea", "pastry", "sandwich"]:
        global current_order
        current_order = order
        print(handle_menu_item(order))
        if order == "coffee" or order == "tea":
            print(ask_for_size())
            size = input()
            print(handle_size(size))
        print(confirm_order())
    else:
        print("I'm sorry, I didn't understand that. Can you please order coffee, tea, pastry, or sandwich?")

chat()    