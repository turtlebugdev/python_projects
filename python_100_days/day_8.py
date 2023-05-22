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
direction = ''
while direction.lower() not in('encode','decode'):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction.lower() not in('encode','decode'):
        print('You must type encode or decode. Try again. ')

text = input("Type your message:\n").lower()
text_check = [*text]
bad_char = []
for t in text_check:
    if t not in alphabet and t != ' ':
        bad_char.append(t)

while  len(bad_char)>0:
    print("The code may only contain letters")
    text = input("Type your message:\n").lower()
    text_check = [*text]
    bad_char = []
    for t in text_check:
        if t not in alphabet and t != ' ':
            bad_char.append(t)
shift = int(input("Type the shift number:\n"))

if direction.lower()  == 'encode':
    def encrypt(text,shift):
        code =''
        for letter in text:
            if letter == ' ':
                code +=' '
            elif alphabet.index(letter)+shift<= len(alphabet)-1:
                code += alphabet[alphabet.index(letter)+shift]
            else:
                code+=  alphabet[alphabet.index(letter)+shift - (len(alphabet))]
        print(code)   
else: #direction.lower() == 'decode':
    def encrypt(text,shift):
        code =''
        for letter in text:
            if letter == ' ':
                code +=' '
            else:
                code += alphabet[alphabet.index(letter)-shift]
        print(code)
encrypt(text,shift)