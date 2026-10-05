print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")
currentbalance=10000
choice=int(input("enter your choice :"))
match choice:
    case 1:
        print(f"Current Balance: {currentbalance}")
    case 2:
        deposit_amount=int(input("Enter deposit amount:"))
        print("Amount deposited successfully")
        updated_balance=currentbalance+deposit_amount
        print(f"Updated Balance: {updated_balance}")  
    case 3:
        withdrawal_amount=int(input("Enter withdrawal amount:"))
        print("Withdrawal successful.")
        remaining_balance=currentbalance-withdrawal_amount
        print(f"Remaining balance: { remaining_balance}")
    case 4:
        print("thank you for using ATM")
    case _:
        print("Invalid Choice")