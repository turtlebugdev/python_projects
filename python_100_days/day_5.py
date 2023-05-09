##### for Loops #####
# fruits = ["Apple", "Peach","Pear"]
# for f in fruits:
#     print(f)
#     print(f + ' Pie')

#### Average Height ####

###Starter code
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)

# #My code
# _sum = 0
# _cnt = 0
# for i in student_heights:
#     _cnt = _cnt + 1
#     _sum = _sum + i
# avg = round(_sum/_cnt)
# print(f"The average of {student_heights} is {avg}")

#### Highest Score ####
## Starter Code
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)

# ## My code below ##
# highest = 0
# for s in student_scores:
#     if s > highest:
#         highest = s

# print(f"The highest score in the class is: {highest}!!")

#### add all numbers 1-100 together ####

# tot = 0
# for n in range(1,101):
#     tot += n
# print(tot)

#### Add all even numbers from 1 - 100 ####
# tot = 0
# for n in range(2,101,2):
#     tot += n
# print(tot)

#### Fizz / Buzz ####

# for n in range(1,101):
#     if n%5==0 and n%3==0:
#         print("FizzBuzz")
#     elif n%5==0:
#         print("Buzz")
#     elif n%3==0:
#         print("Fizz")
#     else:
#         print(n)

#### Password Generator ####
import random
letters =[]
def range_char(start,stop):
    return (chr(l) for l in range(ord(start),ord(stop)+1))

for l in range_char('A','Z'):
    letters.append(l)
for l in range_char('a','z'):
    letters.append(l)
numbers = []
for n in range(0,10):
    numbers.append(str(n))
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?:\n "))
nr_numbers = int(input("How many numbers would you like in your password?:\n "))
nr_symbols = int(input("How many symbols would you like in your password?:\n "))
pw_len = nr_letters+nr_numbers+nr_symbols
let_cnt = 0
num_cnt = 0
sym_cnt = 0
pword = ""
for p in range(1,(pw_len +1)):
    if let_cnt<nr_letters and num_cnt < nr_numbers and sym_cnt < nr_symbols:
        ran_choice = random.choice(['1','2','3']) 
    elif let_cnt<nr_letters and num_cnt < nr_numbers and sym_cnt == nr_symbols:
        ran_choice = random.choice(['1','2'])
    elif let_cnt<nr_letters and num_cnt == nr_numbers and sym_cnt < nr_symbols:
        ran_choice = random.choice(['1','3'])
    elif let_cnt==nr_letters and num_cnt < nr_numbers and sym_cnt < nr_symbols:
        ran_choice = random.choice(['2','3'])
    elif let_cnt==nr_letters and num_cnt == nr_numbers and sym_cnt < nr_symbols:
        ran_choice = '3'
    elif let_cnt==nr_letters and num_cnt < nr_numbers and sym_cnt == nr_symbols:
        ran_choice = '2'
    else:
        ran_choice = '1'

    if ran_choice == '1':
        pword += (random.choice(letters))
        let_cnt += 1
    elif ran_choice == '2':
        pword += (random.choice(numbers))
        num_cnt += 1
    else:
        pword += (random.choice(symbols))
        sym_cnt +=1

print(f"Your new Super Secure PyPassword is: \n {pword}")