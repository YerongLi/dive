# Sample data
data = {
    'a': ['c', 'd'],
    'b': ['d', 'a', 'c'],
    'c': ['a', 'b'],
    'd': ['c', 'a', 'b'],
}

# Step 1) Define has_mutual_first_choice()
def has_mutual_first_choice(username):
    if not len(data[username]) > 0: return False
    b = data[username][0]
    return len(data[b]) > 0 and data[b][0] == username

# Define has_mutual_pair_for_rank()
def has_mutual_pair_for_rank(username, rank):
    if not len(data[username]) > rank: return False
    b = data[username][rank]
    return len(data[b]) > rank and data[b][rank] == username
    return 
# Step 2) Define changed_pairings()
def changed_pairings(username, rank):
    ans = []
    b, c = data[username][rank - 1], data[username][rank]
    # b
    if (len(data[b]) > rank - 1 and data[b][rank - 1] == username) or (len(data[b]) > rank and data[b][rank] == username): ans.append(b)
    # c
    if (len(data[c]) > rank and data[c][rank] == username) or (len(data[c]) > rank - 1 and data[c][rank - 1] == username): ans.append(c)
    return ans
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
