min_balance = 500

current_balance = float(input("Enter your current account balance: Rs."))
withdrawal_amount = float(input("Enter the amount to withdraw: Rs."))

if withdrawal_amount > current_balance:
    print("Insufficient balance. Transaction aborted.")

else:
    
    new_balance = current_balance - withdrawal_amount
    if new_balance < min_balance:
        print(f"Your account balance is Rs.{new_balance}. Please keep your account balance above Rs.500 to avoid unwanted charges.")
    else:
        print(f"Withdrawal successful! Your new balance is Rs.{new_balance}.")
