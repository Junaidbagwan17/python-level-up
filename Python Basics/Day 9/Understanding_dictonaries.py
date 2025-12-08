# dictonaries in Python

months = {"January": "The first month",
          "Decmeber":"the last month"
          }

# edit the dict's value 
months["January"] = "hello"  #{'January': 'hello', 'Decmeber': 'the last month'}


# adding a new key value pair at the last of the dict.
months["june"] = "The middle of the year" #{'January': 'hello', 'Decmeber': 'the last month', 'june': 'The middle of the year'}
# print(months)


#loopin through dict
for key in months:
    print(key) # this gives - january to June
    print(months) # this  prints whole dict
    print(months[key]) # this gives only values of the keys not a key eg. hello to The middle of the year
    
    
#NESTING

travel = {
    "India":{"city_visit" : ["Mumbai", "pune", "Bandra"], "total_visit":12},
    "Saudi":{"city_visit" : ["Jeddha", "Makka", "Riyadh", "Madina"], "total_visits":13}
    }
print(travel)

# --------------# -------------------# -----------------




 ##Python Dictionaries

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
}

#Retrieving items from dictionary.
# print(programming_dictionary["Function"])

#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

#Create an empty dictionary.
empty_dictionary = {}

#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

#Loop through a dictionary
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])

#######################################

#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionary in a List

travel_log = [
  {
    "country": "France", 
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
  },
  {
    "country": "Germany", 
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5
  },
]


