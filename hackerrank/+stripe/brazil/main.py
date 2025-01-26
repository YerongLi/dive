import pandas as pd
def register_receivables(input_string):
    lines = input_string.strip().split("\n")[1:]  # Skip header
    receivables = {}

    for line in lines:
        _, merchant_id, payout_date, card_type, amount = line.split(",")
        key = (merchant_id, card_type, payout_date)
        receivables[key] = receivables.get(key, 0) + int(amount)

    return "merchant_id,card_type,payout_date,amount\n" + "\n".join(
        f"{k[0]},{k[1]},{k[2]},{v}" for k, v in receivables.items()
    )
def update_receivables(registered_csv, contracts_csv):
    registered = {
        tuple(line.split(",")[:3]): int(line.split(",")[3])
        for line in registered_csv.strip().split("\n")[1:]
    }
    contracts = [line.split(",") for line in contracts_csv.strip().split("\n")[1:]]

    updated = [
        (c[0], c[3], c[2], int(c[4])) for c in contracts if registered.pop((c[1], c[3], c[2]), None)
    ]
    updated += [(k[0], k[1], k[2], v) for k, v in registered.items()]

    return "id,card_type,payout_date,amount\n" + "\n".join(
        f"{r[0]},{r[1]},{r[2]},{r[3]}" for r in updated
    )

# Tests
print("Testing register_receivables...")
# Test Case 1: solve1
input1 = """customer_id,merchant_id,payout_date,card_type,amount
cust1,merchantA,2021-12-30,Visa,150
cust2,merchantA,2021-12-30,Visa,200
cust3,merchantB,2021-12-31,MasterCard,300
cust4,merchantA,2021-12-30,Visa,50"""
expected_output1 = """merchant_id,card_type,payout_date,amount
merchantA,Visa,2021-12-30,400
merchantB,MasterCard,2021-12-31,300"""
result1 = register_receivables(input1)
assert result1 == expected_output1, f"Test Case 1 Failed: {result1}"

# Test Case 2: solve1
input2 = """customer_id,merchant_id,payout_date,card_type,amount
cust1,merchantA,2021-12-29,MasterCard,50
cust2,merchantA,2021-12-29,Visa,150
cust3,merchantB,2021-12-31,Visa,300
cust4,merchantB,2021-12-29,MasterCard,200"""
expected_output2 = """merchant_id,card_type,payout_date,amount
merchantA,MasterCard,2021-12-29,50
merchantA,Visa,2021-12-29,150
merchantB,Visa,2021-12-31,300
merchantB,MasterCard,2021-12-29,200"""
result2 = register_receivables(input2)
assert result2 == expected_output2, f"Test Case 2 Failed: {result2}"

print("All Part 1 test cases passed!")

print("Testing update_receivables...")
# Test Case 1: update_receivables
registered_receivables_csv1 = """merchant_id,card_type,payout_date,amount
merchantA,Visa,2022-01-05,500
merchantB,MasterCard,2022-01-06,1000"""
contracts_csv1 = """contract_id,merchant_id,payout_date,card_type,amount
contract1,merchantA,2022-01-05,Visa,500"""
expected_output1 = """id,card_type,payout_date,amount
contract1,Visa,2022-01-05,500
merchantB,MasterCard,2022-01-06,1000"""
result1 = update_receivables(registered_receivables_csv1, contracts_csv1)
assert result1 == expected_output1, f"Test Case 1 Failed: {result1}"

# Test Case 2: update_receivables
registered_receivables_csv2 = """merchant_id,card_type,payout_date,amount
merchantA,Visa,2022-01-07,750
merchantB,MasterCard,2022-01-08,1250
merchantC,Visa,2022-01-09,1500"""
contracts_csv2 = """contract_id,merchant_id,payout_date,card_type,amount
contract1,merchantA,2022-01-07,Visa,750
contract2,merchantC,2022-01-09,Visa,1500"""
expected_output2 = """id,card_type,payout_date,amount
contract1,Visa,2022-01-07,750
contract2,Visa,2022-01-09,1500
merchantB,MasterCard,2022-01-08,1250"""
result2 = update_receivables(registered_receivables_csv2, contracts_csv2)
assert result2 == expected_output2, f"Test Case 2 Failed: {result2}"

print("All Part 2 test cases passed!")
