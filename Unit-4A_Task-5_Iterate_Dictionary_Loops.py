subjects = {
    "Python": 90,
    "Maths": 85,
    "English": 80,
    "Physics": 95
}

print("Keys:")
for key in subjects.keys():
    print(key)

print("\nValues:")
for value in subjects.values():
    print(value)

print("\nItems:")
for key, value in subjects.items():
    print(key, ":", value)