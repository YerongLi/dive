from typing import *
from heapq import *
def solution(items: List[int], start: List[int], end: List[int], query: List[int]) -> List[int]:
	n = len(items)
	d = [0] * n
	for i in range(len(start)):
	  d[start[i]]+= 1
	  d[end[i] + 1]-= 1
	for i in range(1, n):
	  d[i] = d[i - 1] + d[i]
	# d is not count
	xs = set(query)
	xs = list(xs)
	xs.sort()
	mq = {}
	heap = []
	for i, x in enumerate(items):
		heappush(heap, (x, i))
	acc = 0
	for x in xs:
		if heap and heap[0][0] < x:
			_, j = heappop(heap)
			acc+= d[j]
		mq[x] = acc
	ans = []
	for q in query:
		ans.append(mq[q])

	return ans

expected = [2, 5]

# Test Case 1
items = [1, 2, 5, 4, 5]
start = [0, 0, 1]
end = [1, 2, 2]
query = [2, 4]
expected = [2, 5]
result = solution(items, start, end, query)
assert result == expected, f"Test failed: expected {expected}, but got {result}"
