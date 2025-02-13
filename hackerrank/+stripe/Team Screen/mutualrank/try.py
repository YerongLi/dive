# Sample data
data = {
    'a': ['c', 'd'],
    'b': ['d', 'a', 'c'],
    'c': ['a', 'b'],
    'd': ['c', 'a', 'b'],
}

# Step 1) Define has_mutual_first_choice()
def has_mutual_first_choice(username):
    b = data[username][0]
    # [b][0]
    return len(data[b]) > 0 and data[b][0] == username 
# Define has_mutual_pair_for_rank()
def has_mutual_pair_for_rank(username, rank):
    b = data[username][rank]
    return len(data[b]) > rank and data[b][rank] == username

# Step 2) Define changed_pairings()
def changed_pairings(username, rank):
    assert rank > 0, 'Rank has to be positive'
    # [rank] [rank - 1]
    b = data[username][rank - 1]
    c = data[username][rank]
    # [b, c] [c, b]
    def cast(x): return 1 if x else 0

    ans = []
    
    pre, now = has_mutual_pair_for_rank(username, rank - 1) == username, len(data[b]) > rank and data[b][rank] == username
    # pre = cast(pre)
    # now = cast(now)

    if pre ^ now: ans.append(b)

    pre, now = has_mutual_pair_for_rank(username, rank), len(data[c]) > rank - 1 and data[c][rank - 1] == username
    # pre = cast(pre)
    # now = cast(now)
    if pre ^ now: ans.append(c)
    # print(ans)
    return ans

def has_anti_mutual_rank(user, wishlists):
    for r, v in enumerate(wishlists[user]):
        if len(wishlists[v]) > r and wishlists[v][- r - 1] == user: return True
    return False
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

# Test cases
wishlists1 = {
    'a': ['b', 'c', 'd'],  # a's first choice is 'b'
    'b': ['d', 'c', 'a'],  # b's last choice is 'a'
    'c': ['d', 'a'],
    'd': ['c', 'b']
}
assert has_anti_mutual_rank('a', wishlists1) == True  # a and b form an Anti-Mutual Rank

wishlists2 = {
    'a': ['b', 'c', 'd'],
    'b': ['a', 'd', 'c'],  # b does not rank 'a' last
    'c': ['d', 'a', 'b'],
    'd': ['a', 'c']
}
assert has_anti_mutual_rank('a', wishlists2) == True  # 'c' is the antirank of 'a'
wishlists3 = {
    'a': ['b', 'c', 'd'],
    'b': ['d', 'c', 'a'],  # a and b still have an Anti-Mutual Rank
    'c': ['d', 'a'],
    'd': ['c', 'b']
}
assert has_anti_mutual_rank('b', wishlists3) == True  # 'd is the antirank of 'b'



print("All tests passed!")
