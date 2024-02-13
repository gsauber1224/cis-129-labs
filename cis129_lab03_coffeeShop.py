# This program is for calculating total cost of items bought by user at a coffee shop including tax.

# Obtain the number of items purchased from the user
num_coffees = int(input("Number of coffees bought? "))
num_muffins = int(input("Number of muffins bought? "))
num_cookies = int(input("Number of cookies bought? "))
num_teas = int(input("Number of teas bought? "))

# Calculate the subtotal and tax
coffee_price = 5
muffin_price = 4
cookie_price = 3
tea_price = 2
subtotal = (num_coffees * coffee_price) + (num_muffins * muffin_price) (num_cookies * cookie_price) + (num_teas * tea_price)
tax = round(subtotal + 0.06, 2)
total = subtotal + tax

# Display reciept

print('*' * 40)
print("My Coffee and Muffin Shop")
print('*' * 40)
print("Number of items bought:")
print("Coffee:", num_coffees)
print("Muffins:", num_muffins)
print("Cookies:", num_cookies)
print("Teas:", num_teas)
print('*' * 40)
print('*' * 40)
print("My Coffee and Muffin Shop Receipt")
print(f"{num_coffees} Coffee at ${coffee_price} each: ${num_coffees * coffee_price:.2f}")
print(f"{num_muffins} Muffins at ${muffin_price} each: ${num_muffins * muffin_price:.2f}")
print(f"{num_cookies} Cookies at ${cookie_price} each: ${num_cookies * cookie_price:.2f}")
print(f"{num_teas} Teas at ${tea_price} each: ${num_teas * tea_price:.2f}")
print(f"6% tax: ${tax:.2f}")
print("---------")
print(f"Total: ${total:.2f}")
print('*' * 40)

# Thank the user for patronage and invite them to come back soon
print("Thanks for choosing My Coffee and Muffin Shop!")
print("Please come back again soon!")
