# CIS129_Lab7
# Author: Grace Sauber
# Date: March 11, 2024
# This program is designed to calculate income generated from selling theater tickets.


# Set the constants, sections, prices, total seats
SECTIONS = ['A', 'B', 'C']  # List of section names
SEAT_PRICES = {'A': 20, 'B': 15, 'C': 10}  # Section names paired with respective seat prices
SEAT_COUNTS = {'A': 300, 'B': 500, 'C': 200}  # Section names with their available seat counts

# Function for Welcome Message
def display_welcome_message():
    print("Welcome to the Ticket Sales Management System.")
    print("Section Names and Prices:")
    for section in SECTIONS:
        print(f"Section {section}: ${SEAT_PRICES[section]} per seat")
    print()
    # Display available seats in each section
    print("Available seats in each section:")
    for section in SECTIONS:
        print(f"Section {section}: {SEAT_COUNTS[section]} seats")
    print()

# Function to obtain ticket sales while implementing input validation
def get_ticket_sales():
    sales = {}
    for section in SECTIONS:
        while True:
            try:
                num_tickets = int(input(f"Enter the number of tickets sold in section {section}: "))
                if num_tickets < 0:
                    print("Please enter a non-negative number.")
                    continue
                elif num_tickets > SEAT_COUNTS[section]:
                    print(f"Sorry, there are only {SEAT_COUNTS[section]} seats available in section {section}.")
                    continue
                else:
                    sales[section] = num_tickets
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
    return sales

def calculate_subtotal(sales):
 
    # Calculate the subtotal for the current purchase based on the number of tickets sold in each section.
  
  
    subtotal = 0
    for section, num_tickets in sales.items():
        subtotal += num_tickets * SEAT_PRICES[section]
    return subtotal

def main():
  
  # Main function to run the Theater Seating Program.

    display_welcome_message()
    total_sales = 0
    ticketsales = 0
    total_seats_sold = {section: 0 for section in SECTIONS}

    while True:
        # Get ticket sales for the current purchase
        sales = get_ticket_sales()
        # Calculate subtotal for the current purchase
        subtotal = calculate_subtotal(sales)
        # Update total sales
        total_sales += subtotal
        # Update total seats sold in each section
        for section, num_tickets in sales.items():
            total_seats_sold[section] += num_tickets
            SEAT_COUNTS[section] -= num_tickets

        # Display subtotal and total sales so far
        print("Subtotal for this purchase: ${subtotal}")
        print("Total sales so far: ${total_sales}")
        # Display number of seats sold in each section
        print("Number of seats sold in each section:")
        for section, num_seats_sold in total_seats_sold.items():
            print(f"Section {section}: {num_seats_sold} seats sold out of {SEAT_COUNTS[section] + num_seats_sold} total seats")
        print()

        # Ask if the user wants to make another purchase
        if input("Do you want to make another purchase? (yes/no): ").lower() != "yes":
            break

    # Display overall total and number of seats sold in each section
    print("Total Price of Tickets Purchased: ${}".format(total_sales))
    print("Number of seats sold in each section:")
    for section, num_seats_sold in total_seats_sold.items():
        print(f"Section {section}: {num_seats_sold} seats sold out of {SEAT_COUNTS[section] + num_seats_sold} total seats")

if __name__ == "__main__":
    main()
