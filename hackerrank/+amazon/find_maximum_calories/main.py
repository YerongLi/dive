def solution(height):
    height.sort()
    l, r = 0, len(height) - 1
    now = 0
    ans = 0
    while l <= r:
      if abs(height[l] - now) > abs(height[r] - now):
        ans+= (height[l] - now) ** 2

        now = height[l]
        l+= 1
      else:
        ans+= (height[r] - now) ** 2
        now = height[r]
        r-= 1
    return ans

def run_tests():

	# Test Case 1
	height = [5, 2, 5]
	expected = 43
	result = solution(height)
	assert result == expected, f"Test failed: expected {expected}, but got {result}"

	
if __name__ == "__main__":
	run_tests()