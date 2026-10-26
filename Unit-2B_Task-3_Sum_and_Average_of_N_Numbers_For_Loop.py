n = int(input("Enter how many numbers: "))

total = 0

for i in range(n):
    num = int(input("Enter a number: "))
    total = total + num

if n > 0:
    average = total / n
    print("Sum =", total)
    print("Average =", average)
else:
    print("Please enter a positive count")