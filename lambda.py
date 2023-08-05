people = [
    {"name": "Alice", "age": 23},
    {"name": "Sebastian", "age": 21},
    {"name": "Zoey", "age": 20}
]

# Use lambda to sort the dictionaries by age
people.sort(key=lambda person: person["age"])

for person in people:
    print(f"{person['age']}: {person['name']}")
