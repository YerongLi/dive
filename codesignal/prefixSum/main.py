def solution(words):
    N = 10010
    tr = [[0] * 27 for _ in range(N * 50)]
    cn = [0] * N * 50
    idx = 0
    def insert(word):
        nonlocal tr, cn, idx
        p = 0
        for c in word[::-1]:
            o = ord(c) - ord('a')
            if tr[p][o] == 0:
                idx+= 1
                tr[p][o] = idx
            p = tr[p][o]
        cn[p] += 1
    def search(word):
        nonlocal tr, cn, idx
        othercount = 0
        p = 0
        for c in word[::-1]:
            o = ord(c) - ord('a')
            if tr[p][o] == 0: return -1, -1
            othercount+= cn[p]
            p = tr[p][o]
        return othercount, cn[p]
    for word in words:
        insert(word)
    ans = 0
    for word in set(words):
        othercount, count = search(word)
        ans+= othercount * count + (count * (count - 1))//2
    return ans

def test_solution():

    # Test Case 1: One word is a suffix of another
    words = ["apple", "banana", "orange", "e"]
    expected = 2
    result = solution(words)
    assert result == expected, f"Test Case 1 failed. Expected: {expected}, Got: {result}"

    # Test Case 2: Multiple words have the same suffix
    words = ["apple", "pineapple", "banana", "orange", "e"]
    expected = 4
    result = solution(words)
    assert result == expected, f"Test Case 2 failed. Expected: {expected}, Got: {result}"

    # Test Case 3: All words are suffixes of each other
    words = ["back", "backdoor", "door", "comeback", "door"]
    expected = 4
    result = solution(words)
    assert result == expected, f"Test Case 3 failed. Expected: {expected}, Got: {result}"

    # Test Case 4: Random case
    words = ["abcd", "bcde", "cdef", "defg", "efgh"]
    expected = 0  # No suffixes in this case
    result = solution(words)
    assert result == expected, f"Test Case 4 failed. Expected: {expected}, Got: {result}"

    # Test Case 5: All words are the same
    words = ["same", "same", "same", "same"]
    expected = 6  # Combination of 4 choose 2
    result = solution(words)
    assert result == expected, f"Test Case 5 failed. Expected: {expected}, Got: {result}"

    print("All test cases passed successfully.")

# Call the test function
test_solution()
