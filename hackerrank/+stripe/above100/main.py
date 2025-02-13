def redistribute_funds(accounts):
    ll = [[accounts[a], a] for a in accounts]
    ll.sort()
    n = len(ll)
    l, r = 0, n - 1
    ans = []
    for l in range(n):
        toval, to = ll[l]
        if toval < 100:
            while l < r and ll[r][0] >= 100 and ll[l][0] < 100:
                froval, fro = ll[r]
                if froval < 100: return False
                off = min(100 - toval, froval - 100)
                ll[l][0]+= off
                ll[r][0]-= off
                if ll[r][0] == 100: r-= 1
                ans.append({"from": fro, "to": to, "amount": off})
            if l == r and ll[l][0] < 100: return False
    return ans

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
