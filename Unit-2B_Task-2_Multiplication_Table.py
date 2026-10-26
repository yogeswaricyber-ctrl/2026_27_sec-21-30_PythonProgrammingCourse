num = int(input("Enter a number: "))

print("Multiplication Table Using for Loop")
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

print("Multiplication Table Using while Loop")
i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i = i + 1