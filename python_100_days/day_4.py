import random
## Intro to Random Numbers
# random_int = random.randint(1,10)
# print(random_int)
# random_flt = random.random()
# print(random_flt)
# #Create a random number between 1 and 5
# newnum = random.randint(1,4) + random.random()
# print(newnum)

####### Python Coin Flip #######
# flip = random.random()
# if flip >= .5:
#     result = "Heads"
# else:
#     result = "Tails"

# print(result)


###### Lists #####
# states_of_america = ["North Carolina","South Carolina","Florida"]
# fruits = ["apple","pear",'banana']
# fruits.append("grapes")
# fruits[0]="orange"
# print(fruits)

####### Banker's Roulette #######
# diners = []
# number_of_diners = input("How many diners are playing Banker's Roulette?: ")
# appendnum = int(number_of_diners)
# dine_num = 1
# while appendnum > 0:
#     diners.append(input(f"Enter the name of diner number {dine_num}: "))
#     appendnum = appendnum-1
#     dine_num = dine_num+1

# payer = random.choice(diners)
# print(f"The unlucky person paying the whole check will be... {payer}. Everyone should thank {payer} for picking up the bill.")


####### Treasure Map ######
# row1 = ["☐","☐","☐"]
# row2 = ["☐","☐","☐"]
# row3 = ["☐","☐","☐"]
# map = [row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? Enter Column Number followed by Row Number, like 12 for first column, second row. ")

# #Write your code below
# col = int(position[0])-1
# row = int(position[1])-1

# print(f"You chose Column {position[0]} and Row {position[1]} ")

# map[row][col] = "X"
# print(f"{row1}\n{row2}\n{row3}")


####### Rock, Paper, Scissors Game ######

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

P_Choice = input("\nPlease press 'R' for Rock, 'P' for Paper, or 'S' for Scissors.  ")

if P_Choice.upper() == 'R':
    P_Choice = Rock
elif P_Choice.upper() == 'P':
    P_Choice = Paper
elif P_Choice.upper() == 'S':
    P_Choice = Scissors
else:
    print("Error You must type 'R', 'P', or 'S'!!! Try again next time!!")

print(f"\nYou chose\n {P_Choice}")
Poss_Choices = (Rock,Paper,Scissors)
CPU_Choice = random.choice(Poss_Choices)
print(f"\nThe Computer chose\n{CPU_Choice}")

if P_Choice == CPU_Choice:
    print('\nIt is a draw, play again.\n')
elif P_Choice == Rock and CPU_Choice == Scissors:
    print('\nYou Win!!!\n')
elif P_Choice == Rock and CPU_Choice == Paper:
    print('\nYou Lose!!!\n')
elif P_Choice == Scissors and CPU_Choice == Paper:
    print('\nYou Win!!!\n')
elif P_Choice == Scissors and CPU_Choice == Rock:
    print('\nYou Lose!!!\n')
elif P_Choice == Paper and CPU_Choice == Rock:
    print('\nYou Win!!!\n')
else:
    print('\nYou Lose!!!\n')