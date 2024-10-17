from collections import *
def solutionA(inputs):
	ma = OrderedDict()
	mp = {}
	ms = {}
	ans = []
	# INIT
	# CREATE
	# ATTEMPT
	# SUCCESS
	for record in inputs:
		line = record.split()
		if line[0] == 'INIT':
			ma[line[1]] = int(line[2])
		elif line[0] == 'CREATE':
			mp[line[1]] = [line[2], int(line[3])]
			ms[line[1]] = 'CREATE'
		else:
			ms[line[1]] = line[0]
			if line[0] == 'SUCCEED': 
				account, amt = mp[line[1]]
				ma[account]+= amt
	for account in ma:
		ans.append(' '.join([account, str(ma[account])]))
	return ans

def solutionB(inputs):
	ma = OrderedDict()
	mp = {}
	ms = {}
	ans = []
	# INIT
	# CREATE
	# ATTEMPT
	# SUCCESS
	for record in inputs:
		line = record.split()
		if line[0] == 'INIT':
			ma[line[1]] = int(line[2])
		elif line[0] == 'CREATE':
			mp[line[1]] = [line[2], int(line[3])]
			ms[line[1]] = 'CREATE'
		elif line[0] == 'UPDATE' and ms[line[1]] != 'SUCCEED':
			account, _ = mp[line[1]]
			mp[line[1]] = [account, int(line[2])]
		else:
			ms[line[1]] = line[0]
			if line[0] == 'SUCCEED': 
				account, amt = mp[line[1]]
				ma[account]+= amt
	for account in ma:
		ans.append(' '.join([account, str(ma[account])]))
	return ans

def solutionC(inputs):
	ma = OrderedDict()
	mp = {}
	ms = {}
	ans = []
	# INIT
	# CREATE
	# ATTEMPT
	# SUCCESS
	for record in inputs:
		line = record.split()
		if line[0] == 'INIT':
			ma[line[1]] = int(line[2])
		elif line[0] == 'CREATE':
			mp[line[1]] = [line[2], int(line[3])]
			ms[line[1]] = 'CREATE'
		elif line[0] == 'UPDATE' and ms[line[1]] != 'SUCCEED':
			account, _ = mp[line[1]]
			mp[line[1]] = [account, int(line[2])]
		elif line[0] == 'FAILED':
			ms = [line[1]] = 'CREATE'
		elif line[0] == 'REFUND':
			if 
		else:
			ms[line[1]] = line[0]
			if line[0] == 'SUCCEED': 
				account, amt = mp[line[1]]
				ma[account]+= amt
	for account in ma:
		ans.append(' '.join([account, str(ma[account])]))
	return ans

inputs = [
    "INIT m1 0",
    "INIT m2 10",
    "CREATE p1 m1 50",
    "ATTEMPT p1",
    "SUCCEED p1",
    "CREATE p2 m2 100",
    "ATTEMPT p2"
]
expected = ['m1 50', 'm2 10']
ans = solutionA(inputs)
assert expected == ans, "Assertion failed! The output doesn't match the expected result."

inputs = [
    "INIT m1 0",
    "CREATE p1 m1 50",
    "UPDATE p1 100",
    "ATTEMPT p1",
    "SUCCEED p1"
]
expected = ['m1 100']
ans = solutionB(inputs)
assert expected == ans, "Assertion failed! The output doesn't match the expected result."
inputs = [
    "INIT n1 0",
    "CREATE p1 n1 50",
    "ATTEMPT p1",
    "FAIL p1",
    "ATTEMPT p1",
    "SUCCEED p1",
    "CREATE p2 n1 100",
    "ATTEMPT p2",
    "REFUND p2"
]