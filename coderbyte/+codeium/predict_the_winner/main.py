def solution(nums):
	n = len(nums)
	f = [None ] * n
	 
	# [i][j] can Patrick wins or draw

	# for i in range()
def solution(nums):
	n = len(nums)
	f = [[None] * n for _ in range(n)]
	for i in range(n - 1):
		if nums[i] == nums[i + 1]:
			f[i][i + 1] = 0
		else:
			f[i][i + 1] = 1
	for i in range(n - 4, -1, -1):
		for j in range(i + 3, n, 2):
			if nums[i] == nums[j]:
				value = f[i + 1][j - 1]
			else:
				value = 1
			f[i][j] = value
	m = {1:'Patrick', 2: 'Sandy', 0: 'Draw'}
	return m[f[0][n - 1]]
nums = [1, 2, 2, 1]
expected = 'Draw'
result = solution(nums)
assert result == expected, f"Test failed: expected {expected}, but got {result}"


nums = [1, 3, 2, 2, 4, 1]
expected = 'Patrick'
result = solution(nums)
assert result == expected, f"Test failed: expected {expected}, but got {result}"