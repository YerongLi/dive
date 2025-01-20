def calculate_shipping_cost(order, shipping_cost):
    total_cost = 0
    for item in order["items"]:
        product = item["product"]
        quantity = item["quantity"]
        costs = shipping_cost[order["country"]]
        for cost_info in costs:
            if cost_info["product"] == product:
                for cost in cost_info["costs"]:
                    if (cost["maxQuantity"] is None or quantity <= cost["maxQuantity"]) and quantity >= cost["minQuantity"]:
                        total_cost += quantity * cost["cost"]
                        break
    return total_cost

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
                {"minQuantity": 0, "maxQuantity": None, "cost": 550}
            ]
        },
        {
            "product": "laptop",
            "costs": [
                {"minQuantity": 0, "maxQuantity": 2, "cost": 1000},
                {"minQuantity": 3, "maxQuantity": None, "cost": 900}
            ]
        }
    ],
    "CA": [
        {
            "product": "mouse",
            "costs": [
                {"minQuantity": 0, "maxQuantity": None, "cost": 750}
            ]
        },
        {
            "product": "laptop",
            "costs": [
                {"minQuantity": 0, "maxQuantity": 2, "cost": 1100},
                {"minQuantity": 3, "maxQuantity": None, "cost": 1000}
            ]
        }
    ]
}

# Calculate the shipping cost for the US order
total_cost_us = calculate_shipping_cost(order_us, shipping_cost)
print(f"Total shipping cost for US order: {total_cost_us}")

# Calculate the shipping cost for the CA order
total_cost_ca = calculate_shipping_cost(order_ca, shipping_cost)
print(f"Total shipping cost for CA order: {total_cost_ca}")
