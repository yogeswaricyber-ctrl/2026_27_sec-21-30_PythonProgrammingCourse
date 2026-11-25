# Squares of numbers from 1 to 10
squares = [x*x for x in range(1, 11)]

# Even numbers from 1 to 10
even = [x for x in range(1, 11) if x % 2 == 0]

print("Squares:", squares)
print("Even Numbers:", even)