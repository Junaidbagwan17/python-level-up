
travel_log = [
    {
        "country": "India", 
        "cities_visited": ["Mumbai", "Jaipur", "Santacruz", "Rajasthan"],
        "total_visits": 40,
    },
    {
        "country" : "Saudi",
        "cities_visited" : ["Makka", "Madina"],
        "total_visits": 45,
    },
]

# create a one empty dic and append to the travel log using function

def add_new_country(country , city_visited, total_visits):
    new_country = {}
    new_country["country"] = country
    new_country["cities_visited"] = city_visited
    new_country["total_visits"] = total_visits
    travel_log.append(new_country)
    
add_new_country("USA", ["California", "LosAngeles", "WestCost"], 5)
print(travel_log)


# a = [
#     {
#         'country': 'India',
#         'cities_visited': ['Mumbai', 'Jaipur', 'Santacruz', 'Rajasthan'],
#         'total_visits': 40
#      },
#     {
#         'country': 'Saudi',
#         'cities_visited': ['Makka', 'Madina'], 
#         'total_visits': 45
#     },
#     {
#         'country': 'USA',
#         'cities_visited': ['California', 'LosAngeles', 'WestCost'], 
#         'total_visits': 5
#     },
# ]