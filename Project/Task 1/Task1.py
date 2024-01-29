def get_valid_input(prompt, valid_values):
    while True:
        user_input = input(prompt).strip().upper()
        if user_input not in valid_values:
            print(f'Please enter a valid value: {", ".join(valid_values)}')
        else:
            return user_input

# Get the number of pizzas
num_pizzas_str = get_valid_input("How many pizzas do you want to order? Enter a number: ", valid_values=[str(i) for i in range(1, 101)])
num_pizzas = int(num_pizzas_str)

# Check if delivery is required
delivery_required = get_valid_input("Is delivery required? (Y/N) ", valid_values=['Y', 'N'])
delivery_required = delivery_required == 'Y'

# Check if it's Tuesday
is_tuesday = get_valid_input("Is it Tuesday? (Y/N) ", valid_values=['Y', 'N'])
is_tuesday = is_tuesday == 'Y'

# Check if the customer used the app
used_app = get_valid_input("Did the customer use the app? (Y/N) ", valid_values=['Y', 'N'])
used_app = used_app == 'Y'

PIZZA_PRICE = 12.00
DISCOUNT_TUESDAY = 0.5
DISCOUNT_APP = 0.25
DELIVERY_FEE = 2.50
MIN_DELIVERY_ORDER = 5

total_price = num_pizzas * PIZZA_PRICE

if delivery_required:
    if num_pizzas < MIN_DELIVERY_ORDER:
        total_price += DELIVERY_FEE
    else:
        total_price += 0.00

if is_tuesday:
    total_price *= (1 - DISCOUNT_TUESDAY)

if used_app:
    total_price *= (1 - DISCOUNT_APP)


print("\nBPP Pizza Price Calculator")
print("==========================\n")
print(f"How many pizzas ordered? {num_pizzas}")
print(f"Is delivery required? {'Y' if delivery_required else 'N'}")
print(f"Is it Tuesday? {'Y' if is_tuesday else 'N'}")
print(f"Did the customer use the app? {'Y' if used_app else 'N'}\n")
print(f"Total Price: £{total_price:.2f}.")
