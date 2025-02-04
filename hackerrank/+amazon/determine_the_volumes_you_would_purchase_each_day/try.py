def solution(volumes):
	last, r = 0, 0
	n = len(volumes)
	lll = [x for x in range(n + 1)]
	vis = [0] * (n + 1)
	ans = list()
	for x in volumes:
		vis[x] = 1
		if x == r + 1: 
			while r + 1 <= n and vis[r + 1]:
				r+= 1
		if last == r:
			ans.append([-1])
		else:
			ans.append(lll[last + 1: r + 1])
			last = r
	return ans
		
volumes = [2, 1, 4, 3]
expected = [[-1], [1, 2], [-1], [3, 4]] 

result = solution(volumes)
assert result == expected, f"Test failed: expected {expected}, but got {result}"