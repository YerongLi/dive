def compute_penalty(log, remove_at):
    log = log.split()
    n = len(log)
    ans = 0
    for i in range(remove_at):
        if log[i] == '1': ans+= 1
    for i in range(remove_at, n):
        if log[i] == '0': ans+= 1
    return ans

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
    log = log.split()
    n = len(log)
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + (1 if log[i] == '1' else 0)
    ans = 0x7f7f7f7f 
    ansi = None
    for i in range(n + 1):
        # after hour i
        newcost = s[i] + (n - i - (s[n] - s[i]))
        # print(i, newcost)
        if ans > newcost:
            ansi = i
            ans = newcost
    print(ansi, ans, 'ans')
    return ansi

def get_best_removal_times(file_contents):
    pass

# Test cases for 1a
assert compute_penalty("0 0 1 0", 0) == 3, "Test case 1a-1 failed"
assert compute_penalty("0 0 1 0", 4) == 1, "Test case 1a-2 failed"

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

for log in test_cases:
    assert find_best_removal_time(log) in find_best_removal_time1(log), f"Test case failed for log: {log}"


# Test cases for 2a
file_contents = "BEGIN BEGIN \nBEGIN 1 1 BEGIN 0 0\n END 1 1 BEGIN"
assert get_best_removal_times(file_contents) == [2], "Test case 2a-1 failed"

print("All tests passed!")

