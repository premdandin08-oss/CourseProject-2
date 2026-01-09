import sys

def bank_details(argv=None):
    if argv is None:
        argv = sys.argv

    if len(argv) == 6:
        script_name = argv[0]
        acc_holder = argv[1]
        acc_number = argv[2]
        acc_type = argv[3]
        balance = float(argv[4])
        transaction = float(argv[5])
    else:
        script_name = argv[0]
        acc_holder = "Rahul Patil"
        acc_number = "SB102345"
        acc_type = "Savings"
        balance = 15000
        transaction = -3000

    initial_balance = balance

    if transaction > 0:
        balance += transaction
        status = "Deposit Successful"
    elif transaction <= balance:
        balance += transaction
        status = "Withdrawal Successful"
    else:
        status = "Transaction Failed - Insufficient Balance"

    return {
        "script_name": script_name,
        "account_holder": acc_holder,
        "account_number": acc_number,
        "account_type": acc_type,
        "initial_balance": initial_balance,
        "transaction": transaction,
        "updated_balance": balance,
        "status": status
    }

if __name__ == "__main__":
    result = bank_details()

    print("Script Name:", result["script_name"])
    print("Account Holder:", result["account_holder"])
    print("Account Number:", result["account_number"])
    print("Account Type:", result["account_type"])
    print("Initial Balance:", result["initial_balance"])
    print("Transaction Amount:", result["transaction"])
    print("Transaction Status:", result["status"])
    print("Updated Balance:", result["updated_balance"])
