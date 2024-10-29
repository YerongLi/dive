base = ord('a')
def solution(newPasswords, oldPasswords):
	q = len(newPasswords)
	ans = []
	for z in range(q):
		a, b = newPasswords[z], oldPasswords[z]
		l, r = 0, 0
		while l < len(a) and r < len(b):
			if a[l] == b[r] or (ord(b[r]) + 26 - ord(a[l])) % 26 == 1:
				l+= 1
				r+= 1
			else:
				l+= 1
		if r == len(b):
			ans.append('YES')
		else:
			ans.append('NO')
	return ans

newPasswords = ["baacbab", "accdb", "baacba"]
oldPasswords = ["abdbc", "ach", "abb"]
expected = ["YES", "NO", "YES"]
result = solution(newPasswords, oldPasswords)
assert result == expected, f"Test failed: expected {expected}, but got {result}"

newPasswords = ["baacbz", "accdb", "baacba"]
oldPasswords = ["abdba", "ach", "abb"]
expected = ["YES", "NO", "YES"]
result = solution(newPasswords, oldPasswords)
assert result == expected, f"Test failed: expected {expected}, but got {result}"
