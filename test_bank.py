from bank import bank_details
def test_default_values():
    result = bank_details(["bank.py"])

    assert result["account_holder"] == "Rahul Patil"
    assert result["account_type"] == "Savings"
    assert result["initial_balance"] == 15000
    assert result["updated_balance"] == 12000
    assert result["status"] == "Withdrawal Successful"

def test_deposit_transaction():
    args = [
        "bank.py",
        "Amit Desai",
        "SB109876",
        "Current",
        "20000",
        "5000"
    ]

    result = bank_details(args)

    assert result["account_holder"] == "Amit Desai"
    assert result["updated_balance"] == 25000
    assert result["status"] == "Deposit Successful"

def test_withdraw_insufficient_balance():
    args = [
        "bank.py",
        "Sneha Kulkarni",
        "SB108888",
        "Savings",
        "3000",
        "-6000"
    ]
    result = bank_details(args)
    assert result["updated_balance"] == 3000
    assert result["status"] == "Transaction Failed - Insufficient Balance"
