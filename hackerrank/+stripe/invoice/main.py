def test_part1():
    send_schedule = {
        -10: "Upcoming",
        0: "New",
        20: "Reminder",
        30: "Due"
    }

    customer_invoices = [
        {"invoice_time": 0, "name": "Alice", "amount": 200},
        {"invoice_time": 1, "name": "Bob", "amount": 100},
    ]

    expected_output = [
        "-10: [Upcoming] Invoice for Alice for 200 dollars",
        "-9: [Upcoming] Invoice for Bob for 100 dollars",
        "0: [New] Invoice for Alice for 200 dollars",
        "1: [New] Invoice for Bob for 100 dollars",
        "20: [Reminder] Invoice for Alice for 200 dollars",
        "21: [Reminder] Invoice for Bob for 100 dollars",
        "30: [Due] Invoice for Alice for 200 dollars",
        "31: [Due] Invoice for Bob for 100 dollars"
    ]

    assert part1(send_schedule, customer_invoices) == expected_output, "Test Part 1 Failed"

def test_part2():
    send_schedule = {
        -10: "Upcoming",
        0: "New",
        20: "Reminder",
        30: "Due"
    }

    customer_invoices = [
        {"invoice_time": 0, "name": "Alice", "amount": 200},
        {"invoice_time": 1, "name": "Bob", "amount": 100},
    ]

    customer_payments = [
        {"payment_time": -9, "name": "Alice", "amount": 100},
        {"payment_time": 1, "name": "Alice", "amount": 50},
        {"payment_time": 0, "name": "Bob", "amount": 100},
    ]

    expected_output = [
        "-10: [Upcoming] Invoice for Alice for 200 dollars",
        "-9: [Upcoming] Invoice for Bob for 100 dollars",
        "0: [New] Invoice for Alice for 100 dollars",
        "20: [Reminder] Invoice for Alice for 50 dollars",
        "30: [Due] Invoice for Alice for 50 dollars",
        "Delinquent customers:",
        "Alice owes 50 dollars"
    ]

    assert part2(send_schedule, customer_invoices, customer_payments) == expected_output, "Test Part 2 Failed"

# Run tests
test_part1()
test_part2()

print("All tests passed!")
