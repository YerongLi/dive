# Define the function
def get_user_features1(user, features):
    ans = []
    for feature in features:
        # abest even
        if 'locations' in feature and user['location'] not in feature['locations']: continue
        if 'abTest' in feature and feature['abTest'] and user['id'] %2 == 1: continue
        ans.append(feature['id']) 
    return ans
def get_user_features2(user, features):
    ans = []
    for feature in features:
        name = feature['id']
        if 'locations' in feature and feature['locations'] and user['location'] not in feature['locations']: continue
        if 'optOut' in user and name in user['optOut']: continue
        if 'optIn' in user and name in user['optIn']:
            ans.append(name)
            continue
        if 'abTest' in feature and feature['abTest'] and user['id'] %2 == 1: continue
        ans.append(name)
    print(ans)
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
