def test_part1():
    users = [
        {"name": "Alice", "plan": "Premium", "begin_date": 0, "duration": 30},
        {"name": "Bob", "plan": "Basic", "begin_date": 1, "duration": 30},
    ]
    expected_output = [
        "-10: [Upcoming] Invoice for Alice for 200 dollars",
        "-9: [Upcoming] Invoice for Bob for 100 dollars",
        "0: [New] Invoice for Alice for 200 dollars",
        "1: [New] Invoice for Bob for 100 dollars",
        "20: [Reminder] Invoice for Alice for 200 dollars",
        "21: [Reminder] Invoice for Bob for 100 dollars",
        "30: [Due] Invoice for Alice for 200 dollars",
        "31: [Due] Invoice for Bob for 100 dollars",
    ]
    assert part1(users) == expected_output, "Test for part1 failed!"

def test_part2():
    users = [
        {"name": "Alice", "plan": "Premium", "begin_date": 0, "duration": 30},
        {"name": "Bob", "plan": "Basic", "begin_date": 1, "duration": 30},
    ]
    changes = [{"name": "Alice", "new_plan": "Basic", "change_date": 5}]
    expected_output = [
        # Adjusted expected output based on part2 changes
    ]
    assert part2(users, changes) == expected_output, "Test for part2 failed!"

def test_part3():
    users = [
        {"name": "Alice", "plan": "Premium", "begin_date": 0, "duration": 30},
        {"name": "Bob", "plan": "Basic", "begin_date": 1, "duration": 30},
    ]
    changes = [
        {"name": "Alice", "new_plan": "Basic", "change_date": 5},
        {"name": "Bob", "extension": 15, "change_date": 3},
    ]
    expected_output = [
        # Adjusted expected output based on part3 changes
    ]
    assert part3(users, changes) == expected_output, "Test for part3 failed!"

if __name__ == "__main__":
    test_part1()
    test_part2()
    test_part3()
    print("All tests passed!")
