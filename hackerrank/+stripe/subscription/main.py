def test_part1():
    users = [
        {"name": "A", "plan": "X", "begin_date": 0, "duration": 30},
        {"name": "B", "plan": "Y", "begin_date": 1, "duration": 15},
    ]
    expected_output = [
        "0: [Welcome] A, subscribe in plan X",
        "1: [Welcome] B, subscribe in plan Y",
        "1: [Upcoming expiration] B, subscribe in plan Y",
        "15: [Upcoming expiration] A, subscribe in plan X",
        "16: [Expired] B, subscribe in plan Y",
        "30: [Expired] A, subscribe in plan X",
    ]
    assert part1(users) == expected_output, "Test for part1 failed!"

def test_part2():
    users = [
        {"name": "A", "plan": "X", "begin_date": 0, "duration": 30},
        {"name": "B", "plan": "Y", "begin_date": 1, "duration": 15},
    ]
    changes = [{"name": "A", "new_plan": "Y", "change_date": 5}]
    expected_output = [
        "0: [Welcome] A, subscribe in plan X",
        "1: [Welcome] B, subscribe in plan Y",
        "1: [Upcoming expiration] B, subscribe in plan Y",
        "5: [Changed] A, subscribe in plan Y",
        "15: [Upcoming expiration] A, subscribe in plan Y",
        "16: [Expired] B, subscribe in plan Y",
        "30: [Expired] A, subscribe in plan Y",
    ]
    assert part2(users, changes) == expected_output, "Test for part2 failed!"

def test_part3():
    users = [
        {"name": "A", "plan": "X", "begin_date": 0, "duration": 30},
        {"name": "B", "plan": "Y", "begin_date": 1, "duration": 15},
    ]
    changes = [
        {"name": "A", "new_plan": "Y", "change_date": 5},
        {"name": "B", "extension": 15, "change_date": 3},
    ]
    expected_output = [
        "0: [Welcome] A, subscribe in plan X",
        "1: [Welcome] B, subscribe in plan Y",
        "1: [Upcoming expiration] B, subscribe in plan Y",
        "3: [Renewed] B, subscribe in plan Y",
        "5: [Changed] A, subscribe in plan Y",
        "15: [Upcoming expiration] A, subscribe in plan Y",
        "16: [Upcoming expiration] B, subscribe in plan Y",
        "30: [Expired] A, subscribe in plan Y",
        "30: [Expired] B, subscribe in plan Y",
    ]
    assert part3(users, changes) == expected_output, "Test for part3 failed!"

if __name__ == "__main__":
    test_part1()
    test_part2()
    test_part3()
    print("All tests passed!")
