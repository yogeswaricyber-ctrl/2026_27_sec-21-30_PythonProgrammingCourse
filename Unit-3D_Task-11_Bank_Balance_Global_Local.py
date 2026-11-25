balance = 1000

def deposit():
    global balance
    balance += 500

def local_balance():
    balance = 2000
    print("Local Balance:", balance)

deposit()
local_balance()

print("Account Balance:", balance)