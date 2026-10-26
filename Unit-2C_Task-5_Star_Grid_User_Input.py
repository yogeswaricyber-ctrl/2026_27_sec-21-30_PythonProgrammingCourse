rows = int(input("Enter grid size (rows and columns): "))
rows = 5

for row_loop_var in range(1, rows + 1): 
    for column_loop_var in range(1, rows + 1):  
        print("*", end=" ")  
    print()  