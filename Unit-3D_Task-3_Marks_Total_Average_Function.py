def marks(a, b, c):
    total = a + b + c
    avg = total / 3
    return total, avg

t, a = marks(80, 90, 85)

print("Total:", t)
print("Average:", a)