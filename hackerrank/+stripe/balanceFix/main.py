def adjust_balances(transactions, platform_account):
    balances = {}
    
    # 计算初始账户余额
    for account, change in transactions:
        balances[account] = balances.get(account, 0) + change
    
    # 处理余额不足的账户
    if platform_account not in balances:
        balances[platform_account] = 0
    
    filled_transactions = []
    for account in list(balances.keys()):
        if account != platform_account and balances[account] < 0:
            shortfall = -balances[account]
            if balances[platform_account] >= shortfall:
                balances[platform_account] -= shortfall
                balances[account] = 0
                filled_transactions.append((platform_account, -shortfall))
            else:
                filled_transactions.append((platform_account, -balances[platform_account]))
                balances[account] += balances[platform_account]
                balances[platform_account] = 0
    
    # 返回余额大于 0 的账户
    return {acc: bal for acc, bal in balances.items() if bal > 0}

def part1(initial_balance, transactions):
    balances = initial_balance.copy()
    for account, change in transactions:
        balances[account] = balances.get(account, 0) + change
    return [(acc, change) for acc, change in transactions if balances[acc] < 0]

def part3(transactions, platform_account):
    balances = {}
    for account, change in transactions:
        balances[account] = balances.get(account, 0) + change
    adjust_balances(transactions, platform_account)
    return filled_transactions

# 测试 part1: 输出余额不足的交易
initial_balance = {"A": 100, "B": 0, "C": 0}
transactions = [("A", 100), ("B", -50), ("C", -100)]
assert part1(initial_balance, transactions) == [("B", -50), ("C", -100)], f"Test failed for part1, got {part1(initial_balance, transactions)}"

# 测试 part3: 处理余额不足，返回填充交易
platform_account = "Platform"
transactions.append((platform_account, 80))
expected_filled_transactions = [(platform_account, -50), (platform_account, -30)]
assert part3(transactions, platform_account) == expected_filled_transactions, f"Test failed for part3, got {part3(transactions, platform_account)}"

