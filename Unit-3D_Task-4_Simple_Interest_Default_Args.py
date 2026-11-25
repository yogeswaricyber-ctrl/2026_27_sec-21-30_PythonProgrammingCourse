def interest(p, t, r=5):
    return (p * t * r) / 100

print("Default Rate:", interest(1000, 2))
print("Explicit Rate:", interest(1000, 2, 10))