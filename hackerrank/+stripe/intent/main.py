from collections import *
def solutionD(inputs):
	ma = OrderedDict()
	mp = {}
	ms = {}
	ml = defaultdict(None)
	mt = {}
	for record in inputs:
		line = record.split()
		timestamp = int(line[0])
		t = line[1]
		if t == 'INIT':
    		# "1 INIT m1 0 5",

			act = line[2]
			ma[act] = int(line[3])
			if len(line) == 5:
				ml[act] = int(line[4])
		else:
			p = line[2]
			if t == 'CREATE':
				_, _, _ , act, amt = line
				amt = int(amt)
				mp[p] = [act, amt]
				ms[p] = t
			elif t == 'ATTEMPT':
				if ms[p] == 'CREATE':
					ms[p] = t
			elif t == 'SUCCEED':
				if ms[p] == 'ATTEMPT':
					act, amt = mp[p]
					ma[act]+= amt
					ms[p] = t
					mt[p] = timestamp
			elif t == 'FAIL':
				if ms[p] == 'ATTEMPT':
					ms[p] = 'CREATE'
			elif t == 'UPDATE':
				if ms[p] == 'ATTEMPT' or ms[p] == 'CREATE':
					act, _ = mp[p]
					mp[p] = [act, int(line[2])]
			elif t == 'REFUND':
				if ms[p] == 'SUCCEED':
					act, amt = mp[p]
					if not ml[act] or ml[act] + mt[p] >= timestamp:
						ma[act]-= amt
						ms[p] = t
			else:
				print(record, 'skip')
	ans = []
	for act, amt in ma.items():
		ans.append(act+ ' '+str(amt))
	return ans


def solutionC(inputs):
	ma = OrderedDict()
	mp = {}
	ms = {}
	for record in inputs:
		line = record.split()
		t = line[0]
		if t == 'INIT':
			act = line[1]
			ma[act] = int(line[2])
		else:
			p = line[1]
			if t == 'CREATE':
				_, _ , act, amt = line
				amt = int(amt)
				mp[p] = [act, amt]
				ms[p] = t
			elif t == 'ATTEMPT':
				if ms[p] == 'CREATE':
					ms[p] = t
			elif t == 'SUCCEED':
				if ms[p] == 'ATTEMPT':
					act, amt = mp[p]
					ma[act]+= amt
					ms[p] = t
			elif t == 'FAIL':
				if ms[p] == 'ATTEMPT':
					ms[p] = 'CREATE'
			elif t == 'UPDATE':
				if ms[p] == 'ATTEMPT' or ms[p] == 'CREATE':
					act, _ = mp[p]
					mp[p] = [act, int(line[2])]
			elif t == 'REFUND':
				if ms[p] == 'SUCCEED':
					act, amt = mp[p]
					ma[act]-= amt
					ms[p] = t
			else:
				print(record, 'skip')
	ans = []
	for act, amt in ma.items():
		ans.append(act+ ' '+str(amt))
	return ans

def solutionD1(inputs):
	ma = OrderedDict()
	ml = defaultdict(None)
	mp = {}
	ms = {}
	mt = {}
	for record in inputs:
		line = record.split()
		timestamp = int(line[0])

		t = line[1]
		if t == 'INIT':
			# " time INIT m1 0 lll",
			ma[line[2]] = int(line[3])
			ml[line[2]] = int(line[4])
		else:
			p = line[2]
			if t == 'CREATE':
				# "2 CREATE p1 m1 100",

				mp[p] = [line[3], int(line[4])]
				ms[p] = t
			elif t == 'ATTEMPT':
				ms[p] = t
			elif t == 'UPDATE':
				if ms[p] == 'ATTEMPT':
					act, _ = mp[p]
					mp[p] = [act, int(line[2])]
			elif t == 'SUCCEED':
				ms[p] = t
				act, amt = mp[p]
				ma[act]+= amt
				mt[p] = timestamp

			elif t == 'REFUND':
				# "11 REFUND p1",
				act, _ = mp[p]
				if ms[p] == 'SUCCEED' and mt[p] + ml[act] >= timestamp:
					act, amt = mp[p]
					ma[act]-= amt
					ms[p] = t
			elif t == 'FAIL':
				ms[p] == 'CREATE'
			else:
				print(record)
				print('skip')
	ans = []
	for act in ma:
		ans.append(' '.join([act, str(ma[act])	]))
	return ans

def solutionC1(inputs):
	ma = OrderedDict()
	mp = {}
	ms = {}
	for record in inputs:

		line = record.split()
		t = line[0]
		if t == 'INIT':
			# "INIT m1 0",
			ma[line[1]] = int(line[2])
		else:
			p = line[1]
			if t == 'CREATE':
				mp[p] = [line[2], int(line[3])]
				ms[p] = t
			elif t == 'ATTEMPT':
				ms[p] = t
			elif t == 'UPDATE':
				if ms[p] == 'ATTEMPT':
					act, _ = mp[p]
					mp[p] = [act, int(line[2])]
			elif t == 'SUCCEED':
				ms[p] = t
				act, amt = mp[p]
				ma[act]+= amt
			elif t == 'REFUND':
				if ms[p] == 'SUCCEED':
					act, amt = mp[p]
					ma[act]-= amt
					ms[p] = t
			elif t == 'FAIL':
				t == 'CREATE'
			else:
				print('skip')
	ans = []
	for act in ma:
		ans.append(' '.join([act, str(ma[act])	]))
	return ans

def solutionA(inputs):
	ma = OrderedDict() # [m, amt, timestamp]
	mp = {} # [m, amt, timestamp]
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
print(' === PART 3')
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
expected = ['n1 50']
ans = solutionC(inputs)
print(ans)
assert expected == ans, "Assertion failed! The output doesn't match the expected result."

print(' === PART 4')
inputs = [
    "1 INIT m1 0 5",
    "2 CREATE p1 m1 100",
    "3 CREATE p2 m1 50",
    "4 ATTEMPT p1",
    "5 ATTEMPT p2",
    "8 SUCCEED p1",
    "10 SUCCEED p2",
    "11 REFUND p1",
    "16 REFUND p2"
]
expected = ['m1 50']

ans = solutionD(inputs)
assert expected == ans, "Assertion failed! The output doesn't match the expected result."
