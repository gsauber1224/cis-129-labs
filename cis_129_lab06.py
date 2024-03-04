# CIS129_GraceSauber_Lab6.py
# Module 6 Lab-6
# Author: Grace Sauber
# Date: March 3, 2024
# This program helps the user decide the amount of hot dog packages and hot dog bun
# packages needed for a cookout, as well as the modulus of the hot dogs left over.

# Obtain the number of people attending the cookout from the user.

def getTotalHotDogs():
  attendees = int(input("Enter the number of people who will be attending the cookout: "))
  hotDogs = int(input("Enter the number of hot dogs each person will be given: "))
  total = attendees * hotDogs
  return total

def showResults(total):
    DOGS = 10
    BUNS = 8
    dogsLeft = (DOGS - total % DOGS) % DOGS
    minDogs = (total // DOGS) + (0 ** (0 ** dogsLeft))
    bunsLeft = (BUNS - total % BUNS) % BUNS 
    minBuns = (total // BUNS) + (0 ** (0 ** bunsLeft))

# Show the results of the hot dog packages and hot dog bun packages needed.

print("Minimum packages of hot dogs needed for cookout:", minDogs)
print("Minimum packages of hot dog buns needed for cookout:", minBuns)
print("Hot dogs remaining:", dogsLeft)
print("Hot dog buns remaining:", bunsLeft)

# Call the main function.
          
def main():
  totalHotDogs = getTotalHotDogs()
  showResults(totalHotDogs)


if __name__ == "__main__":
  main()
