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
diners = []
number_of_diners = input("How many diners are playing Banker's Roulette?: ")
appendnum = int(number_of_diners)
dine_num = 1
while appendnum > 0:
    diners.append(input(f"Enter the name of diner number {dine_num}: "))
    appendnum = appendnum-1
    dine_num = dine_num+1

payer = random.choice(diners)
print(f"The unlucky person paying the whole check will be... {payer}. Everyone should thank {payer} for picking up the bill.")