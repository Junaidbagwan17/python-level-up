# dict in dict
travel_log = { 
    "India": {"cities_visited" : ["Mumbai", "Jaipur", "Santacruz", "Rajasthan"], "total_visits": 40},
    "Saudi": {"cities_visited" : ["Makka", "Madina"],  "total_visits": 45},
}

# nesting a dict inside list

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