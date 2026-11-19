# PSEUDOCODE
# 1. Ask for pizza size, number of toppings, and delivery distance.
# 2. Convert toppings to an integer and distance to a decimal number.
# 3. Set the base cost:
#    - If small, use $8.
#    - Else if large, use $12.
#    - Otherwise, display an error and stop.
# 4. Reject negative toppings or distance.
# 5. Calculate topping cost: toppings multiplied by $1.
# 6. Calculate delivery fee:
#    - If distance is 0, pickup is free.
#    - Else if distance is at most 5 miles, charge $2.
#    - Otherwise, charge $2 plus $1 per mile beyond 5.
# 7. Add base cost, topping cost, and delivery fee.
# 8. Display the total using an f-string.
#
# Assumption: Fractional additional miles are charged proportionally.


# PYTHON CODE

# Gather order details
pizza_size = input("Pizza size (small or large): ").strip().lower()


toppings = int(input("Number of additional toppings: "))
distance = float(input("Delivery distance in miles (0 for pickup): "))


# Determine the base cost
if pizza_size == "small":
    base_cost = 8
elif pizza_size == "large":
    base_cost = 12
else:
    print("Invalid pizza size. Please choose small or large.")

# Validate toppings and distance
if toppings < 0 or not (0 <= distance < float("inf")):
    print("Toppings and distance must be nonnegative, finite numbers.")


# Calculate topping cost
topping_cost = toppings * 1

# Calculate delivery fee
if distance == 0:
    delivery_fee = 0
elif distance <= 5:
    delivery_fee = 2
else:
    delivery_fee = 2 + (distance - 5) * 1

# Calculate total cost
total_cost = base_cost + topping_cost + delivery_fee

# Display the results
print(f"\nPizza cost: ${base_cost:.2f}")
print(f"Toppings cost: ${topping_cost:.2f}")
print(f"Delivery fee: ${delivery_fee:.2f}")
print(f"Total order cost: ${total_cost:.2f}")