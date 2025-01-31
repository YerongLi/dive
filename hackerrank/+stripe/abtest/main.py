# Define the function
def solve1(user, features):
    ans = []
    for feature in features:
        if ('locations' not in feature or  user['location'] in feature['locations']) \
         and (not feature.get('abTest', False) or user['id'] & 1 == 0):
            ans.append(feature['id'])
    print(ans)
    return ans
def solve2(user, features):
    ans = []
    for feature in features:
        if ('locations' not in feature or  user['location'] in feature['locations']) \
         and (not feature.get('abTest', False) or user['id'] & 1 == 0):
            ans.append(feature['id'])
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
    active_features = solve1(user, features)
    assert active_features == expected_results[user["id"]], f"Test failed for {user['name']} (id={user['id']})"



# Test data for users and features
users = [
    {"id": 0, "name": "eva", "location": "US", "optIn": ["annual_sale"]},  # Opt-in user
    {"id": 1, "name": "tess", "location": "US", "optOut": ["annual_sale"]},  # Opt-out user
    {"id": 2, "name": "rahool", "location": "CA", "optIn": ["canada_promotion"]},  # Opt-in user
    {"id": 3, "name": "amanda", "location": "CA", "optOut": []},  # No optIn, No optOut
]

features = [
    {"id": "annual_sale", "locations": ["US"], "abTest": True},
    {"id": "enhanced_comments", "abTest": True},
    {"id": "canada_promotion", "locations": ["CA"]},
]

# Expected results for each user
expected_results = {
    0: {"annual_sale", "enhanced_comments"},  # eva opts in for "annual_sale", so "annual_sale" will be included
    1: {"enhanced_comments"},  # tess opts out of "annual_sale", so only "enhanced_comments" is included
    2: {"canada_promotion", "enhanced_comments"},  # rahool opts in for "canada_promotion"
    3: {"canada_promotion"},  # amanda has no optIn/optOut, should get "canada_promotion"
}

# Run the assertions
for user in users:
    active_features = solve2(user, features)
    assert active_features == expected_results[user["id"]], f"Test failed for {user['name']} (id={user['id']})"

print("All tests passed!")
print("All tests passed!")
