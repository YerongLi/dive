import collections
def solution1(lamps):
    dc = collections.defaultdict(int)
    for i in range(len(lamps)):
        
        dc[lamps[i][0] - lamps[i][1]] += 1
        dc [lamps[i][0] + lamps[i][1] + 1] -=1
        
    arr = sorted(dc.keys())
    best_pos = 0
    best_ilum = 0
    cur = 0
    
    for i in arr:
        cur = dc[i] + cur
        if cur>best_ilum:
            best_ilum = cur
            best_pos = i
    return best_pos


import collections
def solution(lamps):
    intervals = [[lamp[0] - lamp[1], lamp[0] + lamp[1]] for lamp in lamps]
    m = {}
    for interval in intervals:
        m[interval[0]] = m.get(interval[0], 0) + 1
        m[interval[1] + 1] = m.get(interval[1] + 1, 0) -1
    xs = sorted(m.keys())
    maxc = -0xf
    c = 0
    ans = 0xf
    for x in xs:
        c+= m[x]
        if c > maxc:
            ans = x
            maxc = c
    return ans
def solution1(lamps):
    dc = collections.defaultdict(int)
    for i in range(len(lamps)):
        
        dc[lamps[i][0] - lamps[i][1]] += 1
        dc [lamps[i][0] + lamps[i][1] + 1] -=1
        
    arr = sorted(dc.keys())
    best_pos = 0
    best_ilum = 0
    cur = 0
    
    for i in arr:
        cur = dc[i] + cur
        if cur>best_ilum:
            best_ilum = cur
            best_pos = i
    return best_pos


lamps = [[-2, 3], [2, 3], [2, 1]]
expected = solution1(lamps)
result = solution(lamps)
assert result == expected, f"Test Case 0 failed. Expected: {expected}, Got: {result}"
# Test Case 1
lamps = [[-9, 5], [-5, 2], [0, 3], [4, 1], [7, 4]]
expected = solution1(lamps)
result = solution(lamps)
assert result == expected, f"Test Case 1 failed. Expected: {expected}, Got: {result}"

# Test Case 2
lamps = [[-10, 0], [-6, 3], [-3, 1], [0, 2], [3, 0], [7, 5], [9, 2]]
expected = solution1(lamps)
result = solution(lamps)
assert result == expected, f"Test Case 2 failed. Expected: {expected}, Got: {result}"

# Test Case 3
lamps = [[-7, 0], [-4, 1], [-1, 3], [1, 2], [4, 0], [6, 4], [9, 1], [10, 3]]
expected = solution1(lamps)
result = solution(lamps)
assert result == expected, f"Test Case 3 failed. Expected: {expected}, Got: {result}"

# Test Case 4
lamps = [[-8, 3], [-5, 1], [-3, 0], [0, 2], [3, 4], [6, 0], [8, 5]]
expected = solution1(lamps)
result = solution(lamps)
assert result == expected, f"Test Case 4 failed. Expected: {expected}, Got: {result}"

# Test Case 5
lamps = [[-9, 2], [-6, 5], [-2, 1], [0, 3], [3, 4], [5, 0], [9, 2]]
expected = solution1(lamps)
result = solution(lamps)
assert result == expected, f"Test Case 5 failed. Expected: {expected}, Got: {result}"

# Test Case 6
lamps = [[-10, 0], [0, 0], [10, 0]]
expected = solution1(lamps)
result = solution(lamps)
assert result == expected, f"Test Case 6 failed. Expected: {expected}, Got: {result}"

# Test Case 7
lamps = [[-5, 3], [-2, 2], [0, 1], [2, 4], [5, 2]]
expected = solution1(lamps)
result = solution(lamps)
assert result == expected, f"Test Case 7 failed. Expected: {expected}, Got: {result}"

# Test Case 8
lamps = [[-8, 1], [-6, 0], [-3, 5], [0, 2], [4, 0], [7, 3], [10, 2]]
expected = solution1(lamps)
result = solution(lamps)
assert result == expected, f"Test Case 8 failed. Expected: {expected}, Got: {result}"

# Test Case 9
lamps = [[-10, 0], [-7, 3], [-3, 2], [0, 1], [2, 0], [5, 2], [8, 4]]
expected = solution1(lamps)
result = solution(lamps)
assert result == expected, f"Test Case 9 failed. Expected: {expected}, Got: {result}"

# Test Case 10
lamps = [[-9, 4], [-5, 1], [-2, 3], [0, 0], [3, 2], [6, 5], [10, 2]]
expected = solution1(lamps)
result = solution(lamps)
assert result == expected, f"Test Case 10 failed. Expected: {expected}, Got: {result}"

print("All test cases passed successfully.")