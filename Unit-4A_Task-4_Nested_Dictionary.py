students = {
    1: {"name": "Yogeswari", "marks": 90},
    2: {"name": "Megha", "marks": 85},
    3: {"name": "Ravi", "marks": 95}
}

for student in students.values():
    print("Name:", student["name"])
    print("Marks:", student["marks"])
    print()