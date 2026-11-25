def print_details(**kwargs):
    for k, v in kwargs.items():
        print(k, ":", v)

print_details(name="Krishna", age=26, city="Guntur")