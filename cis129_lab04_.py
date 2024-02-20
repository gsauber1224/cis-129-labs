# Module 4 Lab-4
# Author: Grace Sauber
# Date: February 19, 2024
# This program calculates as well as displays store bonus and employee bonus based on monthly sales.
# As well as calculating the percent increase in sales, it also determines the store bonus amount according to set criteria
# and calculates employee bonus based on percentage increase in sales. 
# If the highest bonus amounts are achieved (store bonus amount of $600 and employee bonus of $75), it congratulates employees.



# declare local variables
monthlySales = 0 # monthly sales amount 
storeAmount = 0 # store bonus amount
empAmount = 0 # employee bonus amount
salesIncrease = 0 # percent of sales increase 
prompt = "Enter the monthly sales amount: " # the prompt will be a string literal


# include code to get monthly Sales
monthlySales = float(input(prompt))


# include code to get the Increase in Sales
salesIncrease = float(input("Enter the percent of increase in sales (in decimal format): "))
salesIncrease = salesIncrease / 100 # convert to decimal 


# include code to calculate the Store Bonus (storeAmount)
if monthlySales > 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales > 90000: 
    storeAmount = 4000
elif monthlySales > 80000:
    storeamount = 3000
else:
    storeAmount = 0 


# include code to calculate the Employee Bonus (empAmount)
if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0


    # This code prints bonus info
print("The store bonus amount is $", storeAmount)
print("The employee bonus amoount is $", empAmount)
if storeAmount == 6000 and empAmount == 75: 
    print("Congrats! You have reached the highest bonus amounts possible! ")
