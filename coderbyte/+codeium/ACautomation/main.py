from collections import *
from bisect import *
# Case 2: * 代表任意substring
# "good*morning" search in "goodddmorning good morning"
# return starting index [0, 14]

# "good*morning" search in "goodddmorning good google morning"
# return starting index [0, 14]

# "good*morning" search in "good goodmorning "
# return starting index [5]
def solution(pattern, doc):
	tot = 0
	l = pattern.split('*')
	N = 1 + sum(len(s) for s in l)
	tr = [[0] * 300 for _ in range(N) ]
	cnt = [0] * N
	found = defaultdict(list)
	index = defaultdict(list)
	m = {}
	g = defaultdict(list)
	ne = [0] * N
	tot = 0
	def ins(s):
		nonlocal tot
		p = 0
		for c in s:
			x = ord(c)
			if not tr[p][x]:
				tot+= 1
				tr[p][x] = tot
			p = tr[p][x]
		cnt[p]+= 1
		m[s] = p

	def build():
		q = deque()
		# 0\
		for i in range(300):
			v= tr[0][i]
			if v:
				q.append(v)
		while q:
			x = q.popleft()
			g[ne[x]].append(x)
			for i in range(300):
				v = tr[x][i]
				if v:
					ne[v] = tr[ne[x]][i]
					q.append(v)
				else:
					tr[x][i] = tr[ne[x]][i]

	def query(s):
		p = 0
		for i, c in enumerate(s):
			p = tr[p][ord(c)]
			found[p].append(i)
	def dfs(x):
		for v in g[x]:
			dfs(v)
			found[x].extend(found[v])

	for s in l:
		ins(s)
	build()
	query(doc)
	dfs(0)
	# ans = 0
	ans = []
	# print(q)
	for word in l:
		index[m[word]] = [x - len(word)+ 1 for x in found[m[word]]]
	error = False
	for start in index[m[l[0]]]:
		limit = start + len(l[0])
		for j in range(1, len(l)):
			x = bisect_left(index[m[l[j]]], limit)
			if x == len(l[j]): 
				error = True
				break
			limit = index[m[l[j]]][x] + len(l[j])
		if not error : 
			for j in range(x, len(index[m[l[-1]]])):
				ans.append(doc[start:index[m[l[-1]]][j]+ len(l[-1])] )
	return ans
pattern = "good*morning"
doc = "goodddmorning good morning"
print(solution(pattern, doc))
# ['goodddmorning', 'goodddmorning good morning', 'good morning']


pattern = "a*b"
doc = 'aabb'

print(solution(pattern, doc))
# ['aab', 'aabb', 'ab', 'abb']
# a [0, 1]
# b [2, 3]