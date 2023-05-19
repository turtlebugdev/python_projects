#### Functions ####

#### Simple Function
# def greet():
#     print("Hello.")
#     print("What would you like to do next?")
#     print("I hope you are mindful to obey your robot overlords...")

# greet()

#### Function with input ####
#user = input("Hello user, what is your name? ")
# def greet(user):

#     print(f"Hello {user}.")
#     print(f"{user}, what would you like to do next?")
#     print(f"{user}, I hope you are mindful to obey your robot overlords...")

# greet('Bill')

#### Functions with more than one input (positional argument)####
# def greet_w_2_param(name, _from):
#     print(f"{name} is from {_from}")
# greet_w_2_param('Rob','San Jose')

#### Functions with more than one input (keyword argument)####
# def greet_w_2_param(name, _from):
#     print(f"{name} is from {_from}")
# greet_w_2_param(_from='San Jose', name='Rob')

#### Function for Paint coverage ####

# import math    
# def paint_calc(height,width,cover):
#     cans_to_buy = math.ceil((height*width)/cover)
#     print(f"You need to buy at least {cans_to_buy} cans")

# test_h = int(input('Height of wall (meters): '))
# test_w = int(input('Width of wall (meters): '))
# coverage = 5
# paint_calc(height=test_h,width=test_w,cover=coverage)

#### Prime number checker ####

# def prime_checker(number):
#     prime = True
#     for i in range(2,number):
#         if number%i==0:
#             prime = False
#     if prime == True:
#         print(f"{number} is a prime number!")
#     else:
#         print(f'{number} is not a prime number.')
# n = int(input('Check this number: '))
# prime_checker(number = n)


### Prime number checker for a range ####

# def prime_checker(number):
#     prime = True
#     for i in range(2,number):
#         if number%i==0:
#             prime = False
#     if prime == True:
#         print(f"{number} is a prime number!")

#     # else:
#     #     print(f'{number} is not a prime number.')


# _range = int(input('Up to what range do you want to ID prime numbers?: '))

# for i in range(2,(_range+1)):
#     prime_checker(i)

### Prime number checker for a range, create a list of primes ####

# def prime_checker(number):
#     prime = True
#     for i in range(2,number):
#         if number%i==0:
#             prime = False
#     if prime == True:
#         return True

# def prime_list(_range):
#     primes = []
#     for i in range(2,(_range+1)):
#         if prime_checker(i) == True:
#             primes.append(i)
#     print(primes)

# _rng = int(input('Up to what range do you want to create a list of prime numbers?: '))

# prime_list(_range = _rng)


#### Ceasar Cypher ####
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text,shift):


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

