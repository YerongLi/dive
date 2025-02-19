from collections import defaultdict

def generate_email_schedule(users, changes=None):
    events = defaultdict(list)
    user_plans = {}
    
    # Step 1: Process initial subscriptions
    for user in users:
        name, plan, begin_date, duration = user['name'], user['plan'], user['begin_date'], user['duration']
        user_plans[name] = {'plan': plan, 'end_date': begin_date + duration}
        
        events[begin_date].append(f"[Welcome] {name}, subscribe in plan {plan}")
        events[begin_date + duration - 15].append(f"[Upcoming expiration] {name}, subscribe in plan {plan}")
        events[begin_date + duration].append(f"[Expired] {name}, subscribe in plan {plan}")
    
    # Step 2: Process changes if any
    if changes:
        for change in changes:
            name, change_date = change['name'], change['change_date']
            if 'new_plan' in change:  # Plan change event
                new_plan = change['new_plan']
                user_plans[name]['plan'] = new_plan
                events[change_date].append(f"[Changed] {name}, subscribe in plan {new_plan}")
            elif 'extension' in change:  # Renewal event
                extension = change['extension']
                user_plans[name]['end_date'] += extension
                events[change_date].append(f"[Renewed] {name}, subscribe in plan {user_plans[name]['plan']}")
    
    # Step 3: Recalculate expiration emails due to renewals or changes
    final_events = defaultdict(list)
    for name, data in user_plans.items():
        plan, end_date = data['plan'], data['end_date']
        final_events[end_date - 15].append(f"[Upcoming expiration] {name}, subscribe in plan {plan}")
        final_events[end_date].append(f"[Expired] {name}, subscribe in plan {plan}")
    
    # Merge and sort events
    for date, msgs in final_events.items():
        events[date] = msgs  # Overwrite previous expiration events
    
    return sorted(events.items())

# Test cases
users_1 = [
    {'name': 'A', 'plan': 'X', 'begin_date': 0, 'duration': 30},
    {'name': 'B', 'plan': 'Y', 'begin_date': 1, 'duration': 15}
]
changes_1 = [
    {'name': 'A', 'new_plan': 'Y', 'change_date': 5}
]
changes_2 = [
    {'name': 'A', 'new_plan': 'Y', 'change_date': 5},
    {'name': 'B', 'extension': 15, 'change_date': 3}
]

def format_schedule(schedule):
    return [f"{day}: {', '.join(events)}" for day, events in schedule]

assert format_schedule(generate_email_schedule(users_1)) == [
    "0: [Welcome] A, subscribe in plan X",
    "1: [Welcome] B, subscribe in plan Y",
    "1: [Upcoming expiration] B, subscribe in plan Y",
    "15: [Upcoming expiration] A, subscribe in plan X",
    "16: [Expired] B, subscribe in plan Y",
    "30: [Expired] A, subscribe in plan X"
]

assert format_schedule(generate_email_schedule(users_1, changes_1)) == [
    "0: [Welcome] A, subscribe in plan X",
    "1: [Welcome] B, subscribe in plan Y",
    "1: [Upcoming expiration] B, subscribe in plan Y",
    "5: [Changed] A, subscribe in plan Y",
    "15: [Upcoming expiration] A, subscribe in plan Y",
    "16: [Expired] B, subscribe in plan Y",
    "30: [Expired] A, subscribe in plan Y"
]

assert format_schedule(generate_email_schedule(users_1, changes_2)) == [
    "0: [Welcome] A, subscribe in plan X",
    "1: [Welcome] B, subscribe in plan Y",
    "1: [Upcoming expiration] B, subscribe in plan Y",
    "3: [Renewed] B, subscribe in plan Y",
    "5: [Changed] A, subscribe in plan Y",
    "15: [Upcoming expiration] A, subscribe in plan Y",
    "16: [Upcoming expiration] B, subscribe in plan Y",
    "30: [Expired] A, subscribe in plan Y",
    "30: [Expired] B, subscribe in plan Y"
]

print("All test cases passed!")
