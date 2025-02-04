# Sample data
data = {
    'a': ['c', 'd'],
    'b': ['d', 'a', 'c'],
    'c': ['a', 'b'],
    'd': ['c', 'a', 'b'],
}

# Step 1) Define has_mutual_first_choice()
def has_mutual_first_choice(username):
    first_choice = data[username][0]  # Get the first choice of the user
    return username == data[first_choice][0]  # Check if the first choice is mutual

# Define has_mutual_pair_for_rank()
def has_mutual_pair_for_rank(username, rank):
    # Get the user’s choice at the given rank
    user_choice = data[username][rank]
    # Check if the user’s choice considers them as the same rank (mutual pair)
    return username == data[user_choice][rank]

# Step 2) Define changed_pairings()
def changed_pairings(username, rank):
    affected_users = []
    
    # Identify which pairings will be affected by the change in rank
    for other_user in data:
        if other_user == username:
            continue
        if rank < len(data[other_user]) and data[other_user][rank] == username:
            affected_users.append(other_user)
    return affected_users

# Test Cases

def test_step_1():
    # Test for has_mutual_first_choice
    assert has_mutual_first_choice('a') == True  # a and c are each other's first choice
    assert has_mutual_first_choice('b') == False  # b's first choice is d, but d does not have b as first choice
    assert has_mutual_first_choice('c') == True  # c's first choice is a, but a's first choice is c
    assert has_mutual_first_choice('d') == False  # d and c are each other's first choice

    # Test for has_mutual_pair_for_rank with rank 0 (first choice)
    assert has_mutual_pair_for_rank('a', 0) == True  # a and c are first choice of each other
    assert has_mutual_pair_for_rank('b', 0) == False  # b's first choice does not mutually consider b as first choice

    # Test for has_mutual_pair_for_rank with rank 1 (second choice)
    assert has_mutual_pair_for_rank('a', 1) == True  # a and d are each other's second choice
    assert has_mutual_pair_for_rank('b', 1) == False  # b's second choice does not mutually consider b as second choice

def test_step_2():
    # Test for changed_pairings
    assert changed_pairings('d', 1) == ['a']  # If d's second choice becomes first, a and d lose mutual rank
    assert changed_pairings('b', 2) == ['c']  # If b's third choice becomes second, c and b become mutually ranked pair
    assert changed_pairings('b', 1) == []  # No changes in mutually ranked pairings when b's second choice is bumped

# Run all tests
test_step_1()
test_step_2()

print("All tests passed!")
