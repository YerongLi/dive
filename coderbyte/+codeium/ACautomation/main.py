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
	l = pattern.split('*')
	N = 1+ sum(len(s) for s in l)

	tr = [[0] * 300 for _ in range(N)] 
	cnt = [0] * N
	found = [[] for _ in range(N)]
	ne = [0] * N
	g = [[] for _ in range(N)]
	tot = 0
	m = {}
	def ins(s):
		global tot
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
		# 0
		for i in range(300):
			v =  tr[0][i]
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
	def query(doc):
		p = 0
		for i, c in enumerate(doc):
			p = tr[p][i]
			found[p].append(i)

	# def dfs(x):
	# 	for v in g[x]:
	# 		dfs(v)
	# 		found[x].extend
	for s in l:
		ins(s)
	build()
	query(doc)


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
	ans = []
	for word in l:
		index[m[word]] = sorted([x - len(word)+ 1 for x in found[m[word]]])
	# print(index[m['']])
	index[0] = range(len(doc)+1)
	error = False
	for start in index[m[l[0]]]:
		limit = start + len(l[0])
		for j in range(1, len(l)):
			x = bisect_left(index[m[l[j]]], limit)
			if x == len(index[m[l[j]]]): 
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
expected = ['goodddmorning', 'goodddmorning good morning', 'good morning']
# ['goodddmorning', 'goodddmorning good morning', 'good morning']

pattern = "she*he"
doc = "hesherheshe"
expected = ['sherhe', 'sherheshe']
print(solution(pattern, doc))

assert expected == solution(pattern,doc)

# she [2, 8]
# he [0, 3, 6, 9]
#['sherhe', 'sherheshe']

pattern = "a*b"
doc = 'aabb'
expected = ['aab', 'aabb', 'ab', 'abb']
print(solution(pattern, doc))
assert expected == solution(pattern,doc)
# ['aab', 'aabb', 'ab', 'abb']
# a [0, 1]
# b [2, 3]

pattern = "a*b*"
doc = 'aabbc'
print(solution(pattern, doc))
expected = ['aab', 'aabb', 'aabbc', 'ab', 'abb', 'abbc']
assert expected == solution(pattern,doc)
# ['aab', 'aabb', 'aabbc', 'ab', 'abb', 'abbc']

pattern = '*a*b'
doc = 'caabbc'
expected = ['caab', 'caabb', 'aab', 'aabb', 'ab', 'abb']
print(solution(pattern, doc))
# ['caab', 'caabb', 'aab', 'aabb', 'ab', 'abb']
assert expected == solution(pattern,doc)

pattern = '*a*b*'
doc = 'caabbc'
expected = ['caab', 'caabb', 'caabbc', 'aab', 'aabb', 'aabbc', 'ab', 'abb', 'abbc']


print(solution(pattern, doc))
# ['caab', 'caabb', 'caabbc', 'aab', 'aabb', 'aabbc', 'ab', 'abb', 'abbc']
assert expected == solution(pattern,doc)
