def redistribute_funds(accounts):
    pass
    

def min_redistribute_funds(accounts):
    pass
            


accounts = {"AU": 80, "US": 140, "MX": 110, "SG": 120, "FR": 70}
expected_transactions = [
    {"from": "US", "to": "AU", "amount": 20},
    {"from": "US", "to": "FR", "amount": 20},
    {"from": "MX", "to": "FR", "amount": 10}
]

transactions = redistribute_funds(accounts)
# Apply transactions to simulate user's solution

for t in transactions:
    accounts[t["from"]] -= t["amount"]
    accounts[t["to"]] += t["amount"]

# Ensure all balances are at least 100
for balance in accounts.values():
    assert balance >= 100, f"Balance {balance} is less than 100"

transactions2 = {"David": 70, "Emma": 150, "Frank": 130, "Grace": 90}
expected_transactions2 = [
    {"from": "Emma", "to": "David", "amount": 30},
    {"from": "Frank", "to": "Grace", "amount": 10}
]

txns2 = redistribute_funds(transactions2)
for t in txns2:
    transactions2[t["from"]] -= t["amount"]
    transactions2[t["to"]] += t["amount"]

for balance in transactions2.values():
    assert balance >= 100, f"Balance {balance} is less than 100"
# Additional test cases checking minimum redistribution

print('Part 1 passed')


transactions3 = {"Hannah": 80, "Ian": 140, "Jack": 110, "Kelly": 70}
expected_transactions3 = [{'from': 'Ian', 'to': 'Hannah', 'amount': 20}, {'from': 'Ian', 'to': 'Kelly', 'amount': 20}, {'from': 'Jack', 'to': 'Kelly', 'amount': 10}]

txns3 = min_redistribute_funds(transactions3)
assert len(txns3) == len(expected_transactions3), f"Expected {len(expected_transactions3)} transactions, got {len(txns3)}"
for t in txns3:
    transactions3[t["from"]] -= t["amount"]
    transactions3[t["to"]] += t["amount"]

for balance in transactions3.values():
    assert balance >= 100, f"Balance {balance} is less than 100"


transactions3 = {"Hannah": 50, "Ian": 200, "Jack": 50}
expected_length = 2
txns3 = min_redistribute_funds(transactions3)
assert len(txns3) == expected_length, f"Expected {expected_length} transactions, got {len(txns3)}"
for t in txns3:
    transactions3[t["from"]] -= t["amount"]
    transactions3[t["to"]] += t["amount"]

for balance in transactions3.values():
    assert balance >= 100, f"Balance {balance} is less than 100"


transactions3 = {"Hannah": 60, "Ian": 140, "Jack": 100}
expected_length = 1
txns3 = min_redistribute_funds(transactions3)
assert len(txns3) == expected_length, f"Expected {expected_length} transactions, got {len(txns3)}"
for t in txns3:
    transactions3[t["from"]] -= t["amount"]
    transactions3[t["to"]] += t["amount"]

for balance in transactions3.values():
    assert balance >= 100, f"Balance {balance} is less than 100"



transactions3 = {"Hannah": 40, "Ian": 140, "Jack": 100}
expected_length = 1
txns3 = min_redistribute_funds(transactions3)
assert txns3 is None, 'no solution'
print('Part 2 passed')

print("All test cases passed!")
