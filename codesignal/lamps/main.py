def solution2(lamps):
    # Sort the intervals based on the starting point of each lamp's illumination range
    intervals = sorted([i - r, i + r] for i, r in lamps)
    ans = 0
    start, end = intervals[0]  # Initialize start and end points with the first interval
    
    # Iterate through the sorted intervals
    for l, r in intervals[1:]:
        # Check if there is a gap between the current interval and the previous one
        if l > start:
            # If there is a gap, add the number of integers illuminated by the previous interval
            # up to the start of the current interval
            ans += min(end + 1, l) - start
        
        # Update the start point for the next iteration
        if end > r:
            # If the end of the previous interval extends beyond the current interval,
            # update the start point to the right end of the current interval
            start = max(start, r + 1)
        else:
            # Otherwise, update the start point to the right end of the previous interval
            start = max(end + 1, l)
        
        # Update the end point to the maximum of the current and previous interval's end points
        end = max(r, end)
    
    # Add the number of integers illuminated by the last interval
    ans += end - start + 1
    
    return ans

def solution1(lamps):
    illuminated_coordinates = set()
    for lamp in lamps:
        start = lamp[0] - lamp[1]
        end = lamp[0] + lamp[1]
        for i in range(start, end + 1):
            illuminated_coordinates.add(i)
    
    count = 0
    for coordinate in illuminated_coordinates:
        if sum(1 for lamp in lamps if coordinate >= lamp[0] - lamp[1] and coordinate <= lamp[0] + lamp[1]) == 1:
            count += 1
    
    # return count
def solution(lamps):
    intervals = [[c -r , c + r] for c, r in lamps]
    st, ed = intervals[0]
    intervals = sorted(intervals)
    ans = 0
    print(intervals)
    for l, r in intervals[1:]:
        # st, ed
        # st, l ,ed, r
        # st, l, r, ed
        # st, ed ,l,  r
        if l <= ed and ed < r:
            ans+= (l - st)
            print(st, l - 1)
            st, ed = ed + 1, r
        elif r < ed:
            print(st, l - 1)
            ans+= (l - st)
            st, ed = r + 1, ed
        else:
            st, ed = l, r
    print(st, ed)
    return ans + ed - st + 1





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