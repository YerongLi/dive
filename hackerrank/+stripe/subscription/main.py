schedule = {-15: 'Upcoming expiration', 0 : 'Expired'}
def part1(users):
    ans = []
    for x in users:
        name, plan, begin, du = x['name'], x['plan'], x['begin_date'], x['duration']
        ans.append([begin, -0x7f7f7f7f, 'Welcome', name, plan])
        for offset, tp in schedule.items():
            ans.append([begin+du+offset, offset, tp, name, plan])
    ans.sort()
    res = [f"{time}: [{tp}] {name}, subscribe in plan {plan}" for time, _, tp, name, plan in ans] 
    return res
def part2(users, changes):
    ans = []
    for x in users:
        name, plan, begin, du = x['name'], x['plan'], x['begin_date'], x['duration']
        ans.append([begin, -0x7f7f7f7f, 'Welcome', name, plan])
        for offset, tp in schedule.items():
            ans.append([begin+du+offset, offset, tp, name, plan])
    # changes = [{"name": "A", "new_plan": "Y", "change_date": 5}]
    for x in changes:
        name, plan, time = x['name'], x['new_plan'], x['change_date']
        ans.append([time, -0x7f, 'Changed', name, plan])
    ans.sort()

    m = {}
    for i, (_, _, tp, name, plan) in enumerate(ans):
        if tp == 'Welcome' or tp == 'Changed':
            m[name] = plan
        ans[i][-1] = m[name]
    res = [f"{time}: [{tp}] {name}, subscribe in plan {plan}" for time, _, tp, name, plan in ans]
    return res
def part3(users, changes):
    from bisect import insort
    ans = []
    e = {}
    for x in users:
        name, plan, begin, du = x['name'], x['plan'], x['begin_date'], x['duration']
        e[name] = begin+du
        ans.append([begin, -0x7f7f7f7f, 'Welcome', name, plan])
        for offset, tp in schedule.items():
            ans.append([begin+du+offset, offset, tp, name, plan])
    # changes = [{"name": "A", "new_plan": "Y", "change_date": 5}]
    for x in changes:
        if 'new_plan' in x:
            name, plan, time = x['name'], x['new_plan'], x['change_date']
            ans.append([time, -0x7f7f, 'Changed', name, plan])
        else:
            name, plan, time = x['name'], x['extension'], x['change_date']
            ans.append([time, -0x7f, 'Renewed', name, plan])
 
    ans.sort()

    m = {}
    i = 0
    # for i, (_, _, tp, name, plan) in enumerate(ans):
    while i < len(ans):
        (_, _, tp, name, plan) = ans[i]
        if tp == 'Welcome' or tp == 'Changed':
            m[name] = plan
        elif tp == 'Renewed':
            e[name]+= plan
            for j in range(i + 1, len(ans)):
                if ans[j][2] not in {'Changed', 'Renewed'} and name == ans[j][-2]:
                    ans[j][2] = None
            for offset, tt in schedule.items():
                insort(ans, [offset+e[name], offset, tt, name, e[name]])
        ans[i][-1] = m[name]
        i+= 1
    res = [f"{time}: [{tp}] {name}, subscribe in plan {plan}" for time, _, tp, name, plan in ans if tp]
    return res
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
        "31: [Expired] B, subscribe in plan Y",
    ]
    assert part3(users, changes) == expected_output, "Test for part3 failed!"

if __name__ == "__main__":
    test_part1()
    test_part2()
    test_part3()
    print("All tests passed!")
