from heapq import *
def solution(array, pairs):
	n = len(array)
	
	d = [0] * n
	for a, b in pairs:
		d[a]+= 1
		if b + 1 < n :
			d[b + 1]-= 1

	for i in range(1, n):
		d[i] = d[i] + d[i - 1]
	ans = 0
	heap = []
	acc = 0 
	for i, x in enumerate(array):
		heappush(heap, (x, d[i]))
	while heap:
		x, cnt = heappop(heap)
		if not cnt:
			ans+= acc
		else:
			acc+= cnt
	return ans
array =[1, 2, 3, 2, 4, 5] 
pairs = [[0, 1], [3, 4], [0, 0], [3, 4]]
expected = 12
result = solution(array, pairs)
assert result == expected, f"Test failed: expected {expected}, but got {result}"