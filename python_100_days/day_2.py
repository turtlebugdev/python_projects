# Tip Calculator
# Program takes inputs of total bill, desired tip %, number of payers
# and returns an equal amount for each to pay for the bill + tip
import math

print('Welcome to the tip calculator.')
total_bill = input('What is the total bill? $ ')
diners_num = input('How many people to split the bill? ')
percent_tip = input('What percentage tip would the group like to leave ? 15, 20, or another amount? ')

each_pay_raw = ((float(total_bill) * .01 * float(percent_tip)) + float(total_bill))/float(diners_num)

#rounding up to cents
each_pay = (math.ceil(each_pay_raw *100))*.01


print('Each person should pay: ' + str(each_pay))