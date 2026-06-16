""" API Task: 
• Call this API:
https://jsonplaceholder.typicode.com/users
• Check status code == 200 before processing
• Print Name, Email, Phone of ALL users
• Save all user data to 'users.json'
• Print total number of users fetched
• Handle all exceptions properly"""

import requests
import json

try:
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)

    if response.status_code == 200:

        users = response.json()

        for user in users:
            print("Name:", user["name"])
            print("Email:", user["email"])
            print("Phone:", user["phone"])
            print("-" * 30)

        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)

        print("Total Users:", len(users))

    else:
        print("Failed to fetch data")

except Exception as e:
    print("Error:", e)