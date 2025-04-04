def calculate_shipping_cost1(order, shipping_cost):
    m = {} # [coutnry][item]   
    for country in shipping_cost:
        m[country] = {}
        for item in shipping_cost[country]:
            m[country][item['product']] = item['cost']
    ans = 0
    c = order['country']
    for item in order['items']:
        name = item['product']
        n = item['quantity']
        ans+= m[c][name] * n
    return ans

# 测试用例
order_us = {
    "country": "US",
    "items": [
        {"product": "mouse", "quantity": 20},
        {"product": "laptop", "quantity": 5}
    ]
}

order_ca = {
    "country": "CA",
    "items": [
        {"product": "mouse", "quantity": 20},
        {"product": "laptop", "quantity": 5}
    ]
}

shipping_cost = {
    "US": [
        {"product": "mouse", "cost": 550},
        {"product": "laptop", "cost": 1000}
    ],
    "CA": [
        {"product": "mouse", "cost": 750},
        {"product": "laptop", "cost": 1100}
    ]
}

# 计算并测试结果
assert calculate_shipping_cost1(order_us, shipping_cost) == 16000, "Test case for US order failed"
assert calculate_shipping_cost1(order_ca, shipping_cost) == 20500, "Test case for CA order failed"
print("calculate_shipping_cost1:All test cases passed!")



def calculate_shipping_cost2(order, shipping_cost):
    m = {} # [coutnry][item]   
    for country in shipping_cost:
        m[country] = {}
        for item in shipping_cost[country]:
            m[country][item['product']] = item['costs']
    ans = 0
    c = order['country']
    for item in order['items']:

        name = item['product']
        n = item['quantity']
        for x in m[c][name]:
            uu = x['maxQuantity']
            ll = x['minQuantity']
            if uu and n > uu:
                ans+= (uu - max(ll, 1) + 1) * x['cost']
            elif n >= ll:
                ans+= (n - max(ll, 1) + 1) * x['cost']

    return ans


# Test cases
order_us = {
    "country": "US",
    "items": [
        {"product": "mouse", "quantity": 20},
        {"product": "laptop", "quantity": 5}
    ]
}

order_ca = {
    "country": "CA",
    "items": [
        {"product": "mouse", "quantity": 20},
        {"product": "laptop", "quantity": 5}
    ]
}

shipping_cost = {
    "US": [
        {
            "product": "mouse",
            "costs": [
                {
                    "minQuantity": 0,
                    "maxQuantity": None,
                    "cost": 550
                }
            ]
        },
        {
            "product": "laptop",
            "costs": [
                {
                    "minQuantity": 0,
                    "maxQuantity": 2,
                    "cost": 1000
                },
                {
                    "minQuantity": 3,
                    "maxQuantity": None,
                    "cost": 900
                }
            ]
        }
    ],
    "CA": [
        {
            "product": "mouse",
            "costs": [
                {
                    "minQuantity": 0,
                    "maxQuantity": None,
                    "cost": 750
                }
            ]
        },
        {
            "product": "laptop",
            "costs": [
                {
                    "minQuantity": 0,
                    "maxQuantity": 2,
                    "cost": 1100
                },
                {
                    "minQuantity": 3,
                    "maxQuantity": None,
                    "cost": 1000
                }
            ]
        }
    ]
}

assert calculate_shipping_cost2(order_us, shipping_cost) == 15700, "Test case for US order failed"
assert calculate_shipping_cost2(order_ca, shipping_cost) == 20200, "Test case for CA order failed"

print("calculate_shipping_cost2: All test cases passed!")

def calculate_shipping_cost3(order, shipping_cost):
    m = {} # [coutnry][item]   
    for country in shipping_cost:
        m[country] = {}
        for item in shipping_cost[country]:
            m[country][item['product']] = item['costs']
    ans = 0
    c = order['country']
    for item in order['items']:

        name = item['product']
        n = item['quantity']
        for x in m[c][name]:
            if x['type'] == 'incremental':
                uu = x['maxQuantity']
                ll = x['minQuantity']
                if uu and n > uu:
                    ans+= (uu - max(ll, 1) + 1) * x['cost']
                elif n >= ll:
                    ans+= (n - max(ll, 1) + 1) * x['cost']
            else:
                if n >= ll:
                    ans+= x['cost']

    return ans
shipping_cost = {
    "US": [
        {
            "product": "mouse",
            "costs": [
                {
                    "type": "incremental",
                    "minQuantity": 0,
                    "maxQuantity": None,
                    "cost": 550
                }
            ]
        },
        {
            "product": "laptop",
            "costs": [
                {
                    "type": "fixed",
                    "minQuantity": 0,
                    "maxQuantity": 2,
                    "cost": 1000
                },
                {
                    "type": "incremental",
                    "minQuantity": 3,
                    "maxQuantity": None,
                    "cost": 900
                }
            ]
        }
    ],
    "CA": [
        {
            "product": "mouse",
            "costs": [
                {
                    "type": "incremental",
                    "minQuantity": 0,
                    "maxQuantity": None,
                    "cost": 750
                }
            ]
        },
        {
            "product": "laptop",
            "costs": [
                {
                    "type": "fixed",
                    "minQuantity": 0,
                    "maxQuantity": 2,
                    "cost": 1100
                },
                {
                    "type": "incremental",
                    "minQuantity": 3,
                    "maxQuantity": None,
                    "cost": 1000
                }
            ]
        }
    ]
}

order_us = {
    "country": "US",
    "items": [
        {"product": "mouse", "quantity": 20},
        {"product": "laptop", "quantity": 5}
    ]
}

order_ca = {
    "country": "CA",
    "items": [
        {"product": "mouse", "quantity": 20},
        {"product": "laptop", "quantity": 5}
    ]
}


assert calculate_shipping_cost3(order_us, shipping_cost) == 14700
assert calculate_shipping_cost3(order_ca, shipping_cost) == 19100
print("calculate_shipping_cost3: All test cases passed!")
