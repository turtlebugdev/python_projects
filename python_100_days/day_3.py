# control flow and logical operators 
# Choose your own adventure game

########## Rollercoaster Ticket Program ###############

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("Here is your ticket. Enjoy the ride! ")
# else:
#     print("Sorry, you must be at least 120 cm to ride the rollercoaster")



#
########### Odd or even ##############
# Create a program that checks if a number is od or even

# num = (int(input("Enter an integer to see if it is odd or even. ")))

# if num % 2 == 0:
#     print("This number is even")
# else:
#     print("This number is odd.")


########### Rollercoaster Ticket Program Part 2 #############

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster! ")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Your ticket will cost $5. Enjoy the ride! ")
#     elif age <= 18:
#         print("Your ticket will cost $7. Enjoy the ride! ")
#     else:
#         print("Your ticket will cost $12. Enjoy the ride! ")
# else:
#     print("Sorry, you must be at least 120 cm to ride the rollercoaster.")




######### BMI Calculator ##############
# print("Welcome to the BMI calcultor. Please start by entering your height, feet first then inches. ")
# height_ft = float(input("Please enter your height in feet: "))
# height_in = float(input("Please enter your height in inches: "))
# weight_lb = float(input("enter your weight in lbs: "))

# height_m = ((height_ft * 12) + height_in) * .0254
# weight_kg = weight_lb * 0.453592

# bmi = round(weight_kg/(height_m*height_m),1)

# if bmi < 16.5:
#      print(f"Your BMI is {bmi} you are severly underweight")
# elif bmi < 18.5:
#      print(f"Your BMI is {bmi} you are underweight")
# elif bmi < 25:
#      print(f"Your BMI is {bmi} you are normal weight")
# elif bmi < 30:
#      print(f"Your BMI is {bmi} you are overweight")
# elif bmi < 35:
#      print(f"Your BMI is {bmi} you are obese")
# elif bmi < 40:
#      print(f"Your BMI is {bmi} you are obese class II")
# else:
#      print(f"Your BMI is {bmi} you are obese class III (extreme obesity)")


####### Leap Year Calculator #########

# print("Welcome to the Leap Year Calculator!")
# yr = float(input("Please enter a year to see if it is a leap year. "))

# yr_int = int(yr)

# if yr%4 == 0:
#     if yr%100 == 0:
#         if yr%400 == 0:
#             print(f"{yr_int} is a leap year!")
#         else:
#             print(f"{yr_int} is not a leap year, sorry.")
#     else:
#         print(f"{yr_int} is a leap year!")
# else:
#     print(f"{yr_int} is not a leap year, sorry.")


########### Rollercoaster Ticket Program Part 3 #############

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster! ")
#     age = int(input("What is your age? "))
#     if age < 12:
#         yes_pic = input("Would you like to purchase a photo on the ride for $3, Y or N? ")
#         if yes_pic.lower() == 'y':
#             print("Your ticket will cost $8. Enjoy the ride! ")
#         else:
#             print("Your ticket will cost $5. Enjoy the ride! ")
#     elif age <= 18:
#         yes_pic = input("Would you like to purchase a photo on the ride for $3, Y or N? ")
#         if yes_pic.lower() == 'y':
#             print("Your ticket will cost $10. Enjoy the ride! ")
#         else:
#             print("Your ticket will cost $7. Enjoy the ride! ")
#     else:
#         yes_pic = input("Would you like to purchase a photo on the ride for $3, Y or N? ")
#         if yes_pic.lower() == 'y':
#             print("Your ticket will cost $15. Enjoy the ride! ")
#         else: 
#             print("Your ticket will cost $12. Enjoy the ride! ")
# else:
#     print("Sorry, you must be at least 120 cm to ride the rollercoaster.")


########### Pizza Order Calculator ##############
# Create a program that takes various inputs regarding pizza size and toppings and outputs a total cost
import math

print("Welcome to Python Pizza, let's start your order! ")

p_size = input("What size pizza would you like? S for small, M for medium, and L for large. ")
pep = input("Would you like peperoni on your pizza, Y or N? ")
xchz = input("Would you like extra cheese, Y or N? ")


#cost for size
if p_size.lower() == 's':
    base_cost = int(15)
    size = "small"
elif p_size.lower() == 'm':
    base_cost = int(20)
    size = "medium"
else:
    base_cost = int(25)
    size = "large"

#cost for pep
if pep.lower() == 'y':
    if p_size.lower() == 's':
        pep_cost = int(2)
        pep_y = "with"
    else:
        pep_cost = int(3)
        pep_y = "with"
else:
    pep_cost = 0
    pep_y = "without"

#cost for xtra cheese
if xchz.lower() == 'y':
    chz_cost = int(1)
    chz_y = "with"
else:
    chz_cost = 0
    chz_y = "without"

tot_cost_raw = float(base_cost+pep_cost+chz_cost)
#tot_cost = format(tot_cost_raw, ".2f")
tot_cost = format((math.ceil(tot_cost_raw *100))*.01,".2f")

print(f"Your order for a {size} pizza {pep_y} pepperoni and {chz_y} extra cheese will be ${tot_cost}. We look forward to serving you. ")