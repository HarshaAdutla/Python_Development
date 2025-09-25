capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "India": "Delhi"
}


travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}
print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])


travel_log_2 = {
    "France": {
        "num_of_times_visited": 5,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany":
        {
            "num_of_times_visited": 7,
            "cities_visited": ["Stuttgart", "Berlin"]
        }
}

print(travel_log_2["Germany"]["cities_visited"][0])