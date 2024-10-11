import bisect
def solution(operations):
	xs = []
	ans = []
	for o in operations:
		if o[0] == 1:
			bisect.insort(xs, o[1])
		else:
			l = o[1]
			r = o[1] + o[2] - 1
			m = len(xs)
			il = bisect.bisect_left(xs, l)
			ir = bisect.bisect_left(xs, r)
			if (il == m or xs[il] != l) and (ir == m or xs[ir] != r) and il == ir:
				y = '1'
			else:
				y = '0'
			ans.append(y)

	return ''.join(ans)


import bisect

def solution1(operations):
	obs = []
	res = ""
	for op in operations:
		if op[0] == 1:
			bisect.insort_right(obs, op[1])
		elif op[0] == 2:
			res+=binary_search(obs, op[1], op[2])
	return res

def binary_search(obs, pos, size):
	start = 0
	end = len(obs) - 1
	ub = pos + size
	if obs[0] > ub or pos > obs[-1]:
		return "1"
	while start <= end:
		mid = start + (end - start) // 2
		if pos <= obs[mid] < ub:
			return "0"
		elif obs[mid] < pos:
			start = mid + 1
		else:
			end = mid - 1
	return "1"

def run_tests():
	operations = [[1, 2], [1, 5], [2, 3, 2], [2, 3, 3], [2, 1, 1], [2, 1, 2]]
	
	expected = "1010" # solution1(operations)  # This should be the expected output
	result = solution(operations)     # The actual function being tested
	
	
	# Assert that both results are equal
	assert result == expected, f"Test failed: expected {expected}, but got {result}"
	
	# Test Case 1
	operations = [[1, 2], [1, 5], [2, 3, 2], [2, 3, 3], [2, 1, 1], [2, 1, 2]]
	expected = solution1(operations)
	result = solution(operations)
	assert result == expected, f"Test failed: expected {expected}, but got {result}"

	# Test Case 2
	operations = [[1, 0], [2, 0, 5], [2, 10, 3], [1, 15], [2, 5, 2], [2, 0, 4]]
	expected = solution1(operations)
	result = solution(operations)
	assert result == expected, f"Test failed: expected {expected}, but got {result}"

	# Test Case 3
	operations = [[1, 1], [2, 1, 10], [1, 5], [2, 10, 5], [2, 1, 2], [2, 0, 1]]
	expected = solution1(operations)
	result = solution(operations)
	assert result == expected, f"Test failed: expected {expected}, but got {result}"

	# Test Case 4
	operations = [[1, 3], [2, 3, 5], [1, 8], [2, 10, 3], [2, 3, 4], [2, 0, 2]]
	expected = solution1(operations)
	result = solution(operations)
	assert result == expected, f"Test failed: expected {expected}, but got {result}"

	# Test Case 5
	operations = [[1, 4], [2, 4, 6], [1, 9], [2, 12, 2], [2, 4, 3], [2, 1, 1]]
	expected = solution1(operations)
	result = solution(operations)
	assert result == expected, f"Test failed: expected {expected}, but got {result}"

	# Test Case 6
	operations = [[1, 10], [2, 10, 8], [1, 20], [2, 30, 5], [2, 10, 4], [2, 0, 3]]
	expected = solution1(operations)
	result = solution(operations)
	assert result == expected, f"Test failed: expected {expected}, but got {result}"

	# Test Case 7
	operations = [[1, 5], [2, 5, 10], [1, 10], [2, 15, 5], [2, 5, 3], [2, 0, 2]]
	expected = solution1(operations)
	result = solution(operations)
	assert result == expected, f"Test failed: expected {expected}, but got {result}"

	# Test Case 8
	operations = [[1, 7], [2, 7, 1], [1, 14], [2, 20, 3], [2, 7, 2], [2, 0, 1]]
	expected = solution1(operations)
	result = solution(operations)
	print(f"Expected: {expected}")
	print(f"Result: {result}")
	assert result == expected, f"Test failed: expected {expected}, but got {result}"

	# Test Case 9
	operations = [[1, 6], [2, 6, 4], [1, 12], [2, 18, 1], [2, 6, 3], [2, 0, 2]]
	expected = solution1(operations)
	result = solution(operations)
	print(f"Expected: {expected}")
	print(f"Result: {result}")
	assert result == expected, f"Test failed: expected {expected}, but got {result}"

	# Test Case 10
	operations = [[1, 8], [2, 8, 2], [1, 16], [2, 24, 5], [2, 8, 4], [2, 0, 1]]
	expected = solution1(operations)
	result = solution(operations)
	print(f"Expected: {expected}")
	print(f"Result: {result}")
	assert result == expected, f"Test failed: expected {expected}, but got {result}"
	print("All test cases have passed.")

if __name__ == "__main__":
	run_tests()