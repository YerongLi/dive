def solution(musics, k):
	ans = 0
	n = len(musics)
	musics = [x for x in musics]
	def dfs(i, length, j):
		nonlocal ans, musics, n
		
		if length > ans:
			ans = length
			print(musics[i - length+1:i + 1])
		if i == n:
			return
		original = musics[i]

		if (not i or musics[i - 1] != musics[i]):
			dfs(i + 1, length + 1, j)
		else:
			dfs(i + 1, 0, j)
			if j > 0 :
				musics[i] = '1' if musics[i] == '0' else '0' 
				dfs(i + 1, length + 1, j - 1)
				musics[i] = original
	dfs(0, 0, k)
	return ans
musics = '1001'
k = 1
expected = 3
result = solution(musics, k)
assert result == expected, f"Test failed: expected {expected}, but got {result}"
