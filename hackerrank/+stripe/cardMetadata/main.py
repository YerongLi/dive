def solutionD(inputs):
	BIN = inputs[0]
	n = inputs[1]
	anslist = [x.split(',') for x in inputs[2:]]
	anslist.sort(key = lambda x : [x[0], -int(x[1])])
	first = 0
	for i in range(n):
		if anslist[first][1] < anslist[i][0]:
			if anslist[first][2] != anslist[i][2]:
				e = str(int(anslist[i][0]) - 1)
				e = '0' * (10 - len(e)) + e
				anslist[first][1] = e
				first = i
			else:
				e = anslist[i][1]
				anslist[first][1] = e
				anslist[i][0] = None
		if i == 0:
			anslist[i][0] = '0' * 10
		if i == n -1:
			anslist[first][1] = '9' * 10
	ans = []
	for x in anslist:
		if x[0]: ans.append(','.join([BIN+x[0], BIN+x[1], x[2]]))
	return ans
def solutionC(inputs):
	BIN = inputs[0]
	n = inputs[1]
	anslist = [x.split(',') for x in inputs[2:]]
	anslist.sort(key = lambda x : [x[0], -int(x[1])])
	first = 0
	for i in range(n):
		if anslist[first][1] < anslist[i][0]:
			e = str(int(anslist[i][0]) - 1)
			e = '0' * (10 - len(e)) + e
			anslist[first][1] = e
			first = i
		if i == 0:
			anslist[i][0] = '0' * 10
		if i == n -1:
			anslist[first][1] = '9' * 10
	ans = []
	for x in anslist:
		ans.append(','.join([BIN+x[0], BIN+x[1], x[2]]))
	return ans

def solutionA(inputs):
	BIN= inputs[0]
	n = inputs[1]
	anslist = [x.split(',') for x in inputs[2:]]
	anslist.sort()
	anslist[0][0] = '0' * 10
	anslist[n - 1][1] = '9' * 10
	ans = []
	for x in anslist:
		ans.append(','.join([BIN+x[0], BIN+x[1],x[2]]))
	# return x
	return ans

def solutionC1(inputs):
	BIN = inputs[0]
	N = inputs[1]
	anslist = [x.split(',') for x in inputs[2:]]
	anslist.sort(key = lambda x: [x[0], -int(x[1])])
	first = 0
	for i in range(N):
		if i == 0:
			anslist[i][0] = '0' * 10


		if anslist[i][0] > anslist[first][1]:
			e = str(int(anslist[i][0]) - 1)
			e =  '0' * (10 - len(e)) + e
			anslist[first][1] = e
			first = i
		if i == N - 1:
			anslist[first][1] = '9' * 10
	ans = []
	for x in anslist:
		ans.append(','.join([BIN+x[0],BIN+x[1],x[2]]))
	return ans

def solutionD1(inputs):
	BIN = inputs[0]
	N = inputs[1]
	anslist = [x.split(',') for x in inputs[2:]]
	anslist.sort(key = lambda x: [x[0], -int(x[1])])
	first = 0
	for i in range(N):
		if i == 0:
			anslist[i][0] = '0' * 10

		# print(i, first, anslist[i][0] , anslist[first][1], anslist[i][0] > anslist[first][1])
		if anslist[i][0] > anslist[first][1]:
			print(anslist[i][2], anslist[first][2])
			
			if anslist[i][2] != anslist[first][2]:  
				e = str(int(anslist[i][0]) - 1)
				e =  '0' * (10 - len(e)) + e
				anslist[first][1] = e
				first = i
			else:
				e = anslist[i][1]
				anslist[first][1] = e
				anslist[i][0] = None
		if i == N - 1:
			anslist[first][1] = '9' * 10
	ans = []
	for x in anslist:
		if x[0]: ans.append(','.join([BIN+x[0],BIN+x[1],x[2]]))
	return ans

def solutionZ(inputs):
	BIN = inputs[0]
	N = inputs[1]
	ans = []
	for i in range(N):
		start, end, t = inputs[i + 2].split(',')
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



print(' === PART 1')
inputs = ['424242',
2,
'4000000000,8999999999,MASTERCARD',
'1000000000,3999999999,VISA']
expected = ['4242420000000000,4242423999999999,VISA', '4242424000000000,4242429999999999,MASTERCARD']

ans = solutionA(inputs)
assert expected == ans, "Assertion failed! The output doesn't match the expected result."

# for row in ans: print(row)
print(' === PART 2')

inputs = ['424242',
2,
'0000000000,3700000000,MASTERCARD',
'6100000000,9999999999,VISA']
ans = solutionB(inputs)
# for row in ans: print(row)
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

print(' === PART 4')
inputs = [
    '424242',  # card number
    2,  # number of records
    '0000000000,5999999999,VISA',
    '6000000000,9999999999,VISA'
]
expected = ['4242420000000000,4242429999999999,VISA']
ans = solutionD(inputs)
# print(ans)
assert expected == ans, "Assertion failed! The output doesn't match the expected result."
inputs = [
    '424242',  # card number
    3,  # number of records
    '1000000000,3999999999,VISA',
    '5000000000,6999999999,VISA',
    '8000000000,9999999999,MASTERCARD'
]
expected = ['4242420000000000,4242427999999999,VISA', 
'4242428000000000,4242429999999999,MASTERCARD']

ans = solutionD(inputs)

assert expected == ans, "Assertion failed! The output doesn't match the expected result."
print()