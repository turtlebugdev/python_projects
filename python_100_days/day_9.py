#### Dictioinaries ####
# Dictionary syntax: Dictionary_Name = {key:value, key:value}
# Example: 
# import fnmatch
# IT_terms = {
#     "bug":"An error in a program that prevents it from running as expected.",
#     "function": "a piece of code you can call within a program.",
#     "loop":"The action of doing something over and over again",
#     }

# # retrieve from dictionary: Dictionary_Name[key]
# IT_terms["bug"]

# # adding to dictionary: Dictionary_Name[new_key] = definition

# IT_terms["hard_drive"] = "Part of computer hardware for storing information or programs."

# # print(IT_terms)

# # IT_terms['bug'] = 'A moth inside the computer flying around.'
# # print(IT_terms)
# # looping through a dictionary
# for i in IT_terms:
#     print(f"{i} =  {IT_terms[i]}")


#### Grading Program ####
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# #🚨 Don't change the code above 👆

# #First *fork* your copy. Then copy-paste your code below this line 👇
# #Finally click "Run" to execute the tests

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# for s in student_scores:
#     if student_scores[s]>= 91:
#         student_grades[s] = 'Outstanding'
#     elif student_scores[s]>= 81:
#         student_grades[s] = 'Exceeds Expectations'
#     elif student_scores[s]>= 71:
#         student_grades[s] = 'Acceptable'
#     else:
#         student_grades[s] = 'Failed'

# print(student_scores)
# print(student_grades)

# #🚨 Don't change the code below 👇

# #### Nesting #####
# capitals = {
#     "France":"Paris",
#     "Germany":"Berlin",
# }

# # Nesting a list in a dictionary
# travel_log = {
#     "France" : ["Paris","Lille","Dijon"],
#     "Germany" : ["Berlin","Hamburg","Stuttgart"],
# }

# # Nesting a list in a list
# my_list = ['a','b',['c','d'],'e']

# # Nesting a dictionary in a dictionary
# travel_log2 = {
#     "France" :{
#         'cities_visited':{
#             'Paris':{
#                 'order':'first',
#                 'arrival_date':'1/2/22',
#                 'departure_date':'1/9/22',
#             },
#             'Lille':{
#                 'order':'second',
#                 'arrival_date':'1/9/22',
#                 'departure_date':'1/16/22',
#             },
#             'Dijon':{
#                 'order':'third',
#                 'arrival_date':'1/23/22',
#                 'departure_date':'1/30/22',
#             },
#         },
#         'date_of_country_entry': '1/2/2022',
#     },
#     "Germany" : {
#         'cities_visited':{
#             "Berlin":{
#                 'order':'first',
#                 'arrival_date':'1/30/22',
#                 'departure_date':'2/6/22',
#             },
#             "Hamburg":{
#                 'order':'second',
#                 'arrival_date':'2/13/22',
#                 'departure_date':'2/20/22',
#             },
#             "Stuttgart":{
#                 'order':'third',
#                 'arrival_date':'2/20/22',
#                 'departure_date':'2/27/22',
#             },
#         },
#         'date_of_country_entry': '1/30/2022',
#     },

# }
# print(travel_log2['Germany'])

# #### Update Travel log through a function ####

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country,visits,cities):
#   newadd = {}
#   newadd["country"] = country
#   newadd["visits"] = visits
#   newadd['cities'] = cities
#   travel_log.append(newadd)




# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2])