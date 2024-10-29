def solution(volumes):
	n = len(volumes)
	vis = [0] * (n + 1)
	ans = []
	l, r = 1, 0
	lll = [i for i in range(n + 1)]
	for x in volumes:
		vis[x] = 1
		while r + 1 <= n and vis[r + 1]:
			r+= 1
		if l <= r:
			ans.append(lll[l: r+1])
			l = r + 1
		else:
			ans.append([-1])
	return ans
volumes = [2, 1, 4, 3]
expected = [[-1], [1, 2], [-1], [3, 4]] 

result = solution(volumes)
assert result == expected, f"Test failed: expected {expected}, but got {result}"