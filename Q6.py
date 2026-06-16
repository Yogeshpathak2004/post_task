""" List & Tuple Operations: 
• Create a list of 8 city names
• Print first 4 cities
• Print last 4 cities
• Add a new city at end
• Remove the first city
• Convert list to tuple and print"""

cities = [
    "Mumbai",
    "Delhi",
    "Pune",
    "Bangalore",
    "Chennai",
    "Hyderabad",
    "Kolkata",
    "Ahmedabad"
]

print("First 4 Cities:", cities[:4])
print("Last 4 Cities:", cities[-4:])

cities.append("Jaipur")
print(cities)

cities.pop(0)
print(cities)

city_tuple = tuple(cities)
print(city_tuple)
