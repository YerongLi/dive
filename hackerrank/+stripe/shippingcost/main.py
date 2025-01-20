def calculate_shipping_cost1(order, shipping_cost):
    cost_dict = {}
    for country in shipping_cost:
        cost_dict[country] = {}
        for d in shipping_cost[country]:
            cost_dict[country][d['product']] = d['cost']
    ans = 0
    country = order['country']
    for item in order['items']:
        ans+= cost_dict[country][item['product']]* item['quantity']
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
    from bisect import bisect_left
    inf = 0x3f3f3f3f
    cost_dict = {}
    # [country][product] list
    ans = 0
    for country in shipping_cost:
        cost_dict[country] = {}
        for product in shipping_cost[country]:
            cost_dict[country][product['product']] = [[x['maxQuantity'] if x['maxQuantity'] else inf, x] for x in product['costs']]
            cost_dict[country][product['product']].sort()
            acc = 0 # base
            for i, x in enumerate(cost_dict[country][product['product']]):
                # x[1] cache
                cache = x[1]
                cost_dict[country][product['product']][i].append(acc)
                if cache['maxQuantity']: acc+= cache['cost'] * (cache['maxQuantity'] - cache['minQuantity'])


    # bisect_left()
    country = order['country']
    for item in order['items']:
        q = item['quantity']
        name = item['product']
        l = cost_dict[country][name]
        i = bisect_left(l, [q, None])
        # l[i]
        cache = l[i][1]
        print(name, l[i], l[i][2] + (q - max(1, cache['minQuantity']) + 1) * cache['cost'])
        ans+= l[i][2] + (q - max(1, cache['minQuantity']) + 1) * cache['cost']
    print(ans)
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
    pass
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
