students = [
    {"name": "Yogeswari", "marks": 90},
    {"name": "Megha", "marks": 85},
    {"name": "Ravi", "marks": 95}
]

# Ascending order
ascending = sorted(students, key=lambda x: x["marks"])

print("Ascending Order:")
for student in ascending:
    print(student)

# Descending order
descending = sorted(students, key=lambda x: x["marks"], reverse=True)

print("\nDescending Order:")
for student in descending:
    print(student)