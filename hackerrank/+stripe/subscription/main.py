from collections import defaultdict

def generate_notifications(users, changes=None):
    events = defaultdict(list)
    user_info = {}
    
    for user in users:
        name, plan, begin_date, duration = user['name'], user['plan'], user['begin_date'], user['duration']
        user_info[name] = {'plan': plan, 'start': begin_date, 'end': begin_date + duration}
        events[begin_date].append(("Welcome", name, plan))
        events[begin_date + duration - 15].append(("Upcoming expiration", name, plan))
        events[begin_date + duration].append(("Expired", name, plan))
    
    if changes:
        for change in changes:
            name = change['name']
            if 'new_plan' in change:
                user_info[name]['plan'] = change['new_plan']
                events[change['change_date']].append(("Changed", name, change['new_plan']))
            elif 'extension' in change:
                user_info[name]['end'] += change['extension']
                events[change['change_date']].append(("Renewed", name, user_info[name]['plan']))
                new_expiry = user_info[name]['end']
                events[new_expiry - 15].append(("Upcoming expiration", name, user_info[name]['plan']))
                events[new_expiry].append(("Expired", name, user_info[name]['plan']))
    
    return {day: sorted(events[day]) for day in sorted(events)}

users = [
    {"name": "A", "plan": "X", "begin_date": 0, "duration": 30},
    {"name": "B", "plan": "Y", "begin_date": 1, "duration": 15},
]
expected_output_1 = {
    0: [("Welcome", "A", "X")],
    1: [("Welcome", "B", "Y"), ("Upcoming expiration", "B", "Y")],
    15: [("Upcoming expiration", "A", "X")],
    16: [("Expired", "B", "Y")],
    30: [("Expired", "A", "X")],
}
assert generate_notifications(users) == expected_output_1

changes_1 = [{"name": "A", "new_plan": "Y", "change_date": 5}]
expected_output_2 = {
    0: [("Welcome", "A", "X")],
    1: [("Welcome", "B", "Y"), ("Upcoming expiration", "B", "Y")],
    5: [("Changed", "A", "Y")],
    15: [("Upcoming expiration", "A", "Y")],
    16: [("Expired", "B", "Y")],
    30: [("Expired", "A", "Y")],
}
assert generate_notifications(users, changes_1) == expected_output_2

changes_2 = [
    {"name": "A", "new_plan": "Y", "change_date": 5},
    {"name": "B", "extension": 15, "change_date": 3},
]
expected_output_3 = {
    0: [("Welcome", "A", "X")],
    1: [("Welcome", "B", "Y"), ("Upcoming expiration", "B", "Y")],
    3: [("Renewed", "B", "Y")],
    5: [("Changed", "A", "Y")],
    15: [("Upcoming expiration", "A", "Y")],
    16: [("Upcoming expiration", "B", "Y")],
    30: [("Expired", "A", "Y"), ("Expired", "B", "Y")],
}
assert generate_notifications(users, changes_2) == expected_output_3

