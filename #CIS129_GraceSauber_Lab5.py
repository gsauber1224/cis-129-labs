#CIS129_GraceSauber_Lab5.py
# Module 5 Lab-4=5
# Author: Grace Sauber
# Date: February 26, 2024
# This program tracks the total number of bottles returned to a grocery store over the course of a week and calculates the total payout for the bottles. 


# Lab 5 The Bottle Return Program

# Step 1: Declare variables

totalBottles = 0  # Variable that stores the total number of bottles that were returned.
totalpayout = 0.0 # Variable that stores the total payout for the returned bottles.
keepGoing = "y" # Variable that controls whether the program keeps running or not. 

# Step 2: Implement Loop to run this program again
while keepGoing.lower() == "y":
    # Step 3: Code that sets the value of these variables
    total_bottles = 0
    counter = 1
    while counter <= 7:
        print("Enter the number of bottles returned for day", counter, ":")
        today_bottles = int(input())
        total_bottles += today_bottles
        counter += 1

        total_payout = total_bottles * 0.10

    # code that prints the total number of bottles as well as total payout
    print("Total number of bottles returned:", total_bottles)
    print("Total payout: $", total_payout)

    print("Do you want to enter another week's worth of data?")
    print("(Enter y or n)")
    keepGoing = input().strip().lower()
    