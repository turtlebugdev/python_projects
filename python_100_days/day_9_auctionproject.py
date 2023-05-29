import os
clear = lambda: os.system('cls')
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
name_bid = {}

def newbid():
    name = input("Enter the bidder's name: ")
    bid = int(input(f"Enter {name}'s bid amount in dollars:$ "))
    name_bid[name] = bid

print(logo)
print("\nWelcome to our silent auction! Let the bidding begin! ")
bidding = True
while bidding == True:
    newbid()
    if input("Are there any other bidders, 'yes'/'no'? ").lower() == 'yes':
        clear()
    else:
        bidding = False
        clear()
winners = []
winning_bid = (max(name_bid.values()))
for n in name_bid:
    if name_bid[n] == winning_bid:
        winners.append(n)

print(f"The lucky winner(s) is/are {winners} with a high bid of {winning_bid}! Everyone congratulate them on their good fortune! ")
# for n in name_bid:
#     print(n)
#     print(name_bid[n])