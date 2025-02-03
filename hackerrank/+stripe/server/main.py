def compute_penalty(log, remove_at):
    log = log.split()
    n = len(log)
    penalty = 0

    for i in range(remove_at):
        if log[i] == '1':
            penalty += 1

    for i in range(remove_at, n):
        if log[i] == '0':
            penalty += 1

    return penalty

def find_best_removal_time(log):
    log = log.split()
    n = len(log)
    min_penalty = float('inf')
    best_time = 0

    for remove_at in range(n + 1):
        penalty = compute_penalty(' '.join(log), remove_at)
        if penalty < min_penalty:
            min_penalty = penalty
            best_time = remove_at

    return best_time

def get_best_removal_times(file_contents):
    logs = []
    current_log = []
    inside_log = False

    for line in file_contents.splitlines():
        for token in line.split():
            if token == "BEGIN":
                if inside_log:
                    current_log = []
                inside_log = True
            elif token == "END":
                if inside_log and current_log:
                    logs.append(' '.join(current_log))
                inside_log = False
            elif inside_log:
                current_log.append(token)

    best_times = [find_best_removal_time(log) for log in logs]
    return best_times

# Test cases for 1a
assert compute_penalty("0 0 1 0", 0) == 3, "Test case 1a-1 failed"
assert compute_penalty("0 0 1 0", 4) == 1, "Test case 1a-2 failed"

# Test cases for 1b
assert find_best_removal_time("0 0 1 1") == 2, "Test case 1b-1 failed"

# Test cases for 2a
file_contents = "BEGIN BEGIN \nBEGIN 1 1 BEGIN 0 0\n END 1 1 BEGIN"
assert get_best_removal_times(file_contents) == [2], "Test case 2a-1 failed"

print("All tests passed!")

