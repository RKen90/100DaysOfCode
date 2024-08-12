capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list in a dictionary

travel_log = {
    "Egypt": ["Cairo", "Alexandria", "Rashitan", "Hurghada"]
}

print(travel_log["Egypt"])

# Printing Alexandria from travel_log
print(travel_log["Egypt"][1])

# Nested Lists
nested_list = ["A", "B", ["C", "D"]]
# Printing from the nested list
print(nested_list[2][1])


# Nesting a dictionary inside a dictionary
travel_logs = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "num_times_visited": 8,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
    }
}

print(travel_logs["Germany"]["cities_visited"][2])