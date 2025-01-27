# Define the function
def get_user_features(user, features):
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
    active_features = get_user_features(user, features)
    assert active_features == expected_results[user["id"]], f"Test failed for {user['name']} (id={user['id']})"

print("All tests passed!")
