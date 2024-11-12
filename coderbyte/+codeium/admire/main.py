def solution(favorite, scores):
	n = len(favorite)
	d = [0] * (n + 1)
	for ii, f in enumerate(favoriate):
		i = ii + 1
		d[f]+= 1

	q = deque()
	for i in range(1, n + 1):
		if not d[i]:
			q.append(i)

	return 0

favorite = [2, 3, 1, 1], scores = [7, 1, 3, 24]
