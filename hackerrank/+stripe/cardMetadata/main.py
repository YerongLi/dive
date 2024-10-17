def solutionZ(inputs):
	BIN = inputs[0]
	N = inputs[1]
	ans = []
	for i in range(N):
		start, end, t = inputs[i + 2].split(',')
		ans.append(','.join([BIN+start, BIN+end, t]))
	return ans

def solutionA(inputs):
	BIN = inputs[0]
	N = inputs[1]
	ans = []
	li, hi = 0, 0
	records = sorted(inputs[2:])
	for i in range(N):
		start, end, t = records[i].split(',')
		if i == 0: start = '0' * 10
		if i == N - 1: end = '9' * 10
		ans.append(','.join([BIN+start, BIN+end, t]))
	return ans


def solutionB(inputs):
	BIN = inputs[0]
	N = inputs[1]
	ans = []
	li, hi = 0, 0
	records = sorted(inputs[2:])
	anslist = []
	for i in range(N):
		start, end, t = records[i].split(',')
		if i == 0: start = '0' * 10
		if i == N - 1: end = '9' * 10
		if i > 0: 
			# print('This branch')
			anslist[i - 1][1] = str(int(start) - 1)

		anslist.append([start, end, t])
		# ans.append(','.join([BIN+start, BIN+end, t]))
	for i in range(N):
		ans.append(','.join([BIN+anslist[i][0], BIN+anslist[i][1], anslist[i][2]]))
	return ans


def solutionC(inputs):
	BIN = inputs[0]
	N = inputs[1]
	ans = []
	li, hi = 0, 0
	anslist = [record.split(',') for record in inputs[2:]]
	anslist = [[record[0], record[1], record[2]] for record in anslist]
	anslist.sort(key= lambda x: [x[0], -int(x[1])])
	first = 0
	for i in range(N):
		if i == 0:
			anslist[i][0] = '0' * 10
		if i == N - 1:
			anslist[first][1] = '9' * 10
		if anslist[i][0] > anslist[first][1]:
			s = str(int(anslist[i][0]) - 1)
			ls = len(s)
			s = '0' * (10 - ls)  + s
			anslist[first][1] = s
			first = i
	for i in range(N):
		ans .append(','.join([BIN+anslist[i][0], BIN+anslist[i][1], anslist[i][2]]))
	return ans

def solutionD(inputs):
	BIN = inputs[0]
	N = inputs[1]
	ans = []
	li, hi = 0, 0
	anslist = [record.split(',') for record in inputs[2:]]
	anslist = [[record[0], record[1], record[2]] for record in anslist]
	anslist.sort(key= lambda x: [x[0], -int(x[1])])
	first = 0
	reslist= []
	for i in range(N):
		if i == 0:
			anslist[i][0] = '0' * 10
		if i == N - 1:
			anslist[first][1] = '9' * 10
		if anslist[i][0] > anslist[first][1]:
			s = str(int(anslist[i][0]) - 1)
			ls = len(s)
			s = '0' * (10 - ls)  + s
			anslist[first][1] = s
			first = i

	for i in range(N):
		ans.append(','.join([BIN+anslist[i][0], BIN+anslist[i][1], anslist[i][2]]))
	return ans
print(' === PART 1')
inputs = ['424242',
2,
'4000000000,8999999999,MASTERCARD',
'1000000000,3999999999,VISA']
ans = solutionA(inputs)
for row in ans: print(row)
print()
print(' === PART 2')

inputs = ['424242',
2,
'0000000000,3700000000,MASTERCARD',
'6100000000,9999999999,VISA']
ans = solutionB(inputs)
print(ans)
for row in ans: print(row)
print()

print(' === PART 3')
inputs = [
    '424242',  # card number
    4,  # number of records
    '1000000000,5000000000,VISA',
    '2000000000,4000000000,CB',
    '6000000000,9000000000,CB',
    '7000000000,8000000000,VISA'
]
ans = solutionC(inputs)
expected = ['4242420000000000,4242425999999999,VISA', 
'4242422000000000,4242424000000000,CB', 
'4242426000000000,4242429999999999,CB', 
'4242427000000000,4242428000000000,VISA']

assert expected == ans, "Assertion failed! The output doesn't match the expected result."

print()