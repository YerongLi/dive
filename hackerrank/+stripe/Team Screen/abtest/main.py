# Define the function
from collections import *
def get_user_features1(user, features):
    ans = []
    uid = user['id']
    for feature in features:
        if 'locations' in feature and user['location'] not in feature['locations']: continue
        if 'abTest' in feature and feature['abTest'] and uid % 2 == 1: continue # kip the odd users
        ans.append(feature['id'])
    return ans
def get_user_features2(user, features):
    ans = []
    uid = user['id']
    for feature in features:
        name = feature['id']
        if 'locations' in feature and feature['locations'] and user['location'] not in feature['locations']: continue
        if 'optIn' in user and name in user['optIn']:
            ans.append(name)
            continue
        if 'optOut' in user and name in user['optOut']:
            continue
        if 'abTest' in feature and feature['abTest'] and uid % 2 == 1: continue # kip the odd users
        ans.append(name)
    return ans

def get_user_features3(user, features):
    ans = []
    uid = user['id']
    inf = 0x7f7f7f7f
    com = defaultdict(list)
    for i, feature in enumerate(features):
        name = feature['id']
        if 'optIn' in user and name in user['optIn']:
            features[i]['priority'] = inf   
        elif 'priority' not in features[i]:
            features[i]['priority'] = 0
        com[name].extend(feature.get('incompatible', []))
        for x in feature.get('incompatible', []):
            com[x].append(name)
    vis = set()
    features.sort(key = lambda x: x['priority'], reverse = True)
    for feature in features:
        name = feature['id']
        if name in vis: continue
        if 'locations' in feature and feature['locations'] and user['location'] not in feature['locations']: continue
        if 'optIn' in user and name in user['optIn']:
            ans.append(name)
            vis.add(name)
            for x in com[name]: vis.add(x)
            continue
        if 'optOut' in user and name in user['optOut']:
            continue
        if 'abTest' in feature and feature['abTest'] and uid % 2 == 1: continue # kip the odd users
        ans.append(name)
        vis.add(name)
        for x in com[name]: vis.add(x)

    return ans
# Define test data for users and features
users = [
    {"id": 0, "name": "eva", "location": "US"},
    {"id": 1, "name": "tess", "location": "US"},
    {"id": 2, "name": "rahool", "location": "CA"},
    {"id": 3, "name": "amanda", "location": "CA"}
]

features = [
    {"id": "annual_sale", "locations": ["US"], "abTest": True},
    {"id": "enhanced_comments", "abTest": True},
    {"id": "canada_promotion", "locations": ["CA"]}
]

# Define the expected results for each user
expected_results = {
    0: ["annual_sale", "enhanced_comments"],  # eva (id=0) gets both "annual_sale" and "enhanced_comments"
    1: [],  # tess (id=1) gets nothing because "annual_sale" requires an even id
    2: ["enhanced_comments", "canada_promotion"],  # rahool (id=2) gets both "enhanced_comments" and "canada_promotion"
    3: ["canada_promotion"]  # amanda (id=3) gets only "canada_promotion"
}

# Run the assertions
for user in users:
    active_features = get_user_features1(user, features)
    assert active_features == expected_results[user["id"]], f"Test failed for {user['name']} (id={user['id']})"

print("PART 1: All tests passed!")


# Test data with optIn and optOut
users = [
    {"id": 0, "name": "eva", "location": "US", "optIn": ["annual_sale"]},
    {"id": 1, "name": "tess", "location": "US", "optIn": ["annual_sale"]},
    {"id": 2, "name": "rahool", "location": "CA", "optOut": ["enhanced_comments", "canada_promotion"]},
    {"id": 3, "name": "amanda", "location": "CA", "optIn": ["annual_sale"]}
]

features = [
    {"id": "annual_sale", "locations": ["US"], "abTest": True},
    {"id": "enhanced_comments", "locations": None, "abTest": True},
    {"id": "canada_promotion", "locations": ["CA"], "abTest": False},
    {"id": "test", "locations": ["DE"]}
]

# Expected results
expected_results = {
    0: ["annual_sale", 'enhanced_comments'],  # eva opts in for "annual_sale"
    1: ['annual_sale'],  # tess opts in but ignores ABtest
    2: [],  # rahool opts out of both features
    3: ["canada_promotion"]  # amanda opts in for "annual_sale"
}
# Run assertions
for user in users:
    active_features = get_user_features2(user, features)
    assert active_features == expected_results[user["id"]], f"Test failed for {user['name']} (id={user['id']})"

print("PART 2: All tests passed!")

# Test data with optIn, optOut, and incompatibilities
users = [
    {"id": 0, "name": "eva", "location": "US", "optIn": ["annual_sale"]},
    {"id": 1, "name": "tess", "location": "US", "optIn": ["annual_sale"]},
    {"id": 2, "name": "rahool", "location": "CA", "optOut": ["enhanced_comments", "canada_promotion"]},
    {"id": 3, "name": "amanda", "location": "CA", "optIn": ["lunar_sale"]}
]

features = [
    {"id": "annual_sale", "locations": ["US"], "abTest": True, "priority": 5},
    {"id": "enhanced_comments", "locations": None, "abTest": True, "priority": 2},
    {"id": "canada_promotion", "locations": ["CA"], "abTest": False, "priority": 3},
    {"id": "lunar_sale", "incompatible": ["annual_sale"], "priority": 10},
    {"id": "app_redesign", "incompatible": ["lunar_sale", "enhanced_comments"], "priority": 15, "abTest": True}
]

# Expected results
expected_results = {
    0: ["app_redesign", "annual_sale"],  # eva opts in for "annual_sale", app_redesign wins due to priority
    1: ["annual_sale"],  # tess opts in for "annual_sale"
    2: ["app_redesign"],  # rahool gets "app_redesign" due to priority, opts out of others
    3: ["lunar_sale", "canada_promotion"]  # amanda opts in for "lunar_sale", allowing it over conflicts
}

# Run assertions
for user in users:
    active_features = get_user_features3(user, features)
    assert set(active_features) == set(expected_results[user["id"]]), f"Test failed for {user['name']} (id={user['id']})"
print("PART 3: All tests passed!")
