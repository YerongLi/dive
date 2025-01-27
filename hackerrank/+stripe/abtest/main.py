# Mock implementation of solve1 and solve2
def solve1(features, users):
    results = []
    for user in users:
        user_features = []
        for feature in features:
            if (feature["locations"] is None or user["location"] in feature["locations"]) and (
                not feature["abTest"] or user["id"] % 2 == 0
            ):
                user_features.append(feature["id"])
        results.append(user_features)
    return results

def solve2(features, users):
    results = []
    for user in users:
        user_features = []
        for feature in features:
            if (
                feature["locations"] is None or user["location"] in feature["locations"]
            ) and (
                feature["id"] in user.get("optIn", []) or (
                    feature["id"] not in user.get("optOut", []) and (not feature["abTest"] or user["id"] % 2 == 0)
                )
            ):
                user_features.append(feature["id"])
        results.append(user_features)
    return results

# Helper functions to create feature and user dictionaries
def make_feature(id, locations=None, abTest=False):
    return {"id": id, "locations": locations, "abTest": abTest}

def make_user(id, name, location, optIn=None, optOut=None):
    return {"id": id, "name": name, "location": location, "optIn": optIn or [], "optOut": optOut or []}

# Define test data
features = [
    make_feature("annual_sale", ["US"], True),
    make_feature("enhanced_comments", None, True),
    make_feature("canada_promotion", ["CA"], False),
    make_feature("test", ["DE"]),
]

users_1 = [
    make_user(0, "eva", "US"),
    make_user(1, "tess", "US"),
    make_user(2, "rahool", "CA"),
    make_user(3, "amanda", "CA"),
]

users_2 = [
    make_user(0, "eva", "US", optIn=["annual_sale"]),
    make_user(1, "tess", "US", optIn=["annual_sale"]),
    make_user(2, "rahool", "CA", optOut=["enhanced_comments", "canada_promotion"]),
    make_user(3, "amanda", "CA", optIn=["annual_sale"]),
]

# Run tests for solve1
result1 = solve1(features, users_1)
assert result1 == [
    ["annual_sale"],  # eva (id=0) passes "annual_sale"
    [],  # tess (id=1) fails "annual_sale" because id is odd
    ["canada_promotion"],  # rahool (id=2) passes "canada_promotion"
    ["canada_promotion"],  # amanda (id=3) passes "canada_promotion"
]

# Run tests for solve2
result2 = solve2(features, users_2)
assert result2 == [
    ["annual_sale"],  # eva (id=0) explicitly opts in for "annual_sale"
    ["annual_sale"],  # tess (id=1) explicitly opts in for "annual_sale"
    [],  # rahool (id=2) opts out of "enhanced_comments" and "canada_promotion"
    ["annual_sale"],  # amanda (id=3) explicitly opts in for "annual_sale"
]

print("All tests passed!")
