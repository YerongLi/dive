from collections import defaultdict
import pandas as pd
def register_receivables(input_string):
    l = input_string.splitlines()[1:]
    l = [x.split(',') for x in l]
    ans = defaultdict(int)

    for customer_id,merchant_id,payout_date,card_type,amount in l:
        ans[(merchant_id,payout_date,card_type)]+= int(amount)
    print(ans)
    keys = list(ans.keys())
    ansstr = [f'{merchant_id},{card_type},{payout_date},{ans[(merchant_id,payout_date,card_type)]}' for merchant_id,payout_date,card_type in keys]
    ansstr = '\n'.join(ansstr)
    ansstr = 'merchant_id,card_type,payout_date,amount\n' + ansstr
    return ansstr
def update_receivables(registered_csv, contracts_csv):
    registered = registered_csv.splitlines()[1:]
    registered = [x.split(',') for x in registered]
    contracts = contracts_csv.splitlines()[1:]
    contracts = [x.split(',') for x in contracts]

    ansdict = defaultdict(int)
    # customer_id,merchant_id,payout_date,card_type,amount
    for customer_id,merchant_id,payout_date,card_type,amount in registered:
        ansdict[(merchant_id,card_type,payout_date)]+= int(amount)
    for contract_id,merchant_id,payout_date,card_type,amount in constracts:
        ansdict[(contract_id,card_type,payout_date)]+= int(amount)
        ansdict[(merchant_id,card_type,payout_date)]-= int(amount)
    keys = list(ans.keys())
    for k in keys: if ansdict[k] == 0: del ansdict
    ans = [f'{id_},{card_type},{payout_date},{ansdict[(id_,card_type,payout_date)]}' for id_,card_type,payout_date in ansdict]
    ans = '\n'.join(ans)
    ans = 'id,card_type,payout_date,amount\n' + ans
    return ans 
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
