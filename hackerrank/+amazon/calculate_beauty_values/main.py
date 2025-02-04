from heapq import *
def solution(array, pairs):
	d = [0] * (len(array) + 1)
	for a, b in pairs:
		d[a]+= 1
		d[b+1]-= 1
	m = 0x7f7f7f7f
	for i in range(1, len(array)):
		d[i]+= d[i - 1]
	for i, x in enumerate(array):
		if not d[i]:
			m = min(m, x)
	heap = []
	for i, x in enumerate(array):
		heappush(heap, [x, d[i]])
	ans, acc = 0, 0		
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