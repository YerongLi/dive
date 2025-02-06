def compute_penalty(log, remove_at):
    log = log.split()
    total1 = log.count('1')
    total0 = log.count('0')
    one, zero = 0, 0
    for i in range(remove_at):
        if log[i] == '1':
            one+= 1
        else:
            zero+= 1
    return one+ total0-zero
def find_best_removal_time1(log):
    log = log.split()
    n = len(log)
    min_penalty = 0x7f7f7f7f
    best_time = {0}

    for i in range(n + 1):
        penalty = compute_penalty(' '.join(log), i)
        if penalty < min_penalty:
            min_penalty = penalty
            best_time = {i}
        elif penalty == min_penalty:
            best_time.add(i)

    return best_time

def find_best_removal_time2(log):
    log = log.split()
    n = len(log)
    total_down = log.count('1')
    total_up = log.count('0')

    current_down = 0
    current_up = 0
    min_penalty = 0x7f7f7f7f

    for i in range(n + 1):
        if i > 0:
            if log[i - 1] == '1':
                current_down += 1
            else:
                current_up += 1

        penalty = current_down + (total_up - current_up)
        if penalty < min_penalty:
            min_penalty = penalty
            best_time = {i}
        elif penalty == min_penalty:
            best_time.add(i)

    print(best_time, 'ground_true', min_penalty)
    return best_time

def find_best_removal_time(log):
    n = len(log.split())
    ans = 0x7f7f7f7f
    ansi = {}
    for i in range(n + 1):
        newcost = compute_penalty(log, i)
        if newcost < ans:
            ans = newcost
            ansi = {i}
        elif newcost == ans:
            ansi.add(i) 
    return next(iter(ansi))


def get_best_removal_times(file_contents):
    begin = False
    log = file_contents.split()
    l = []
    ans = []
    for x in log:
        if x == 'BEGIN':
            begin = True
            l.clear()
        elif x == 'END':
            ans.append(find_best_removal_time(' '.join(l)))
            begin = False
        elif begin:
            l.append(x)
    return ans

# Test cases for 1a
assert compute_penalty("0 0 1 0", 0) == 3, "Test case 1a-1 failed"
assert compute_penalty("0 0 1 0", 4) == 1, "Test case 1a-2 failed"
print('Test All passed for Part 1a')
# Test cases for 1b
test_cases = [
    "0 0 1 1",
    "0 0 0 0",
    "1 1 1 1",
    "0 1 0 1",
    "1 0 1 0",
    "0",
    "1",
    "0 1 0 1 0 1",
    "1 0 1 0 1 0",
    "0 0 0 1 0 0 0 1 0 0 0",
    "1 1 1 0 1 1 1 0 1 1 1"
]
print('Test All passed for Part 1b')


for log in test_cases:
    assert find_best_removal_time(log) in find_best_removal_time1(log), f"Test case failed for log: {log}"


# Test cases for 2a
file_contents = "BEGIN BEGIN \nBEGIN 1 1 BEGIN 0 0\n END 1 1 BEGIN"
assert get_best_removal_times(file_contents) == [2], "Test case 2a-1 failed"
print('Test All passed for Part 2b')

print("All tests passed!")

