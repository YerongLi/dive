def solution(nums):
	n = len(nums) 
	left, right = 0, 0
	for i in range(0, n - 1):
		if nums[i] > nums[i + 1]:
			left+= nums[i] - nums[i + 1]
		else:
			right+= nums[i + 1] - nums[i]
	return left + right + abs(nums[0] - left) 
# Test Case 1
nums = [2, 4 , 4]

expected = 4
result = solution(nums)
assert result == expected, f"Test failed: expected {expected}, but got {result}"

nums = [2, -2, -3, -1]
expected = 10
result = solution(nums)
assert result == expected, f"Test failed: expected {expected}, but got {result}"
