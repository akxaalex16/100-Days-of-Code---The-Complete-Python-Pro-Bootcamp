example_nesting = {
    "Key": ["List"],
    "Key2": {dict}}

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# nested list in dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}

# print Lille
print(travel_log["France"][1])

nested_list = ["a", "b", ['c', 'd']]

# print d
print(nested_list[2][1])

travel_logs = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 8
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 12,
    }
}

# print Stuttgart
print(travel_logs['Germany']['cities_visited'][2])

# checking for the highest value in a dictionary
fruits = {
    "apple": 2,
    "pear": 4,
    "orange": 9
}

print(max(fruits, key=fruits.get))