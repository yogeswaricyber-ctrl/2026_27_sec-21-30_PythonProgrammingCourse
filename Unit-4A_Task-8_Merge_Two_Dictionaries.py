dict1 = {"a": 10, "b": 20}
dict2 = {"c": 30, "d": 40}

# Create a copy of the first dictionary
merged = dict1.copy()

# Merge second dictionary
merged.update(dict2)

print("First Dictionary:", dict1)
print("Second Dictionary:", dict2)
print("Merged Dictionary:", merged)