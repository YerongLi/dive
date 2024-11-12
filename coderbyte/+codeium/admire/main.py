from collections import *
def solution(favorite, scores):
	n = len(favorite)
	d = [0] * (n + 1)
	for ii, f in enumerate(favorite):
		# i = ii + 1
		d[f]+= 1

	q = deque()
	for i in range(1, n + 1):
		if not d[i]:
			q.append(i)
	ans = 0
	while q:

		u = q.popleft()
		v = favorite[u - 1]
		ans+= scores[u - 1]

		d[v]-= 1
		if not d[v]:
			q.append(v)
	m = None
	for x in range(1, n + 1):
		if d[x]:
			if not m or scores[m - 1] > scores[x - 1]:
				m = x
	for x in range(1, n + 1):
		if d[x] and x != m:
			ans+= scores[x - 1]
	print(ans)
	return ans

favorite = [2, 3, 1, 1]
scores = [7, 1, 3, 24]

expected = 34
assert solution(favorite, scores) ==  expected
