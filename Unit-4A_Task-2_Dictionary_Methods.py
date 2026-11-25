student = {
    "name": "Nagasri",
    "age": 18,
    "course": "B.Tech"
}

print("Keys:", student.keys())

print("Values:", student.values())

print("Items:", student.items())

print("Get Name:", student.get("name"))

student.update({"age": 19})
print("After Update:", student)

student.pop("course")
print("After Pop:", student)