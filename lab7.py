p=int(input("Enter the principal amount in rupee"))
r=int(input("Enter the rate at interest in percentage"))
t=int(input("Enter the time"))
A=p*(1+r/100)**t
print(A)