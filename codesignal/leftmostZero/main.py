import bisect
def solution(state, operations):
    zeros = [i for i, x in enumerate(state) if x == 0]
    for o in operations:
        if o == 'L':
            if zeros:
                state[zeros[0]] = 1
                del zeros[0]
        else:
            x = int(o[2:-1])
            if state[x]:
                state[x] = 0
                bisect.insort(zeros, x)
    return state
    # return state

def solution1(state, operations):
    # 初始化一个存储0的位置的列表
    zero_positions = [i for i, value in enumerate(state) if value == 0]

    for op in operations:
        if op == "L":
            # 如果还有0的位置，就取第一个0的位置，并将其设置为1
            if zero_positions:
                first_zero_pos = zero_positions.pop(0)
                state[first_zero_pos] = 1
        elif op.startswith("C"):
            # 提取C操作后的索引i，并将其设置为0
            _, index = op.split("(")
            index = int(index[:-1])  # 去掉右括号并转换为整数
            state[index] = 0
            # 将位置i按顺序插入到zero_positions中
            # 保持zero_positions的有序性，可以使用二分查找来找到插入位置
            insert_pos = bisect.bisect_left(zero_positions, index)
            # 如果这个位置不在列表中，就插入它
            if insert_pos == len(zero_positions) or zero_positions[insert_pos] != index:
                zero_positions.insert(insert_pos, index)

    return state


# Test Case 1
state = [0, 1, 0, 1, 0]
operations = ["L", "C(0)", "L", "C(2)", "L"]
expected = solution1(state[:], operations)
result = solution(state[:], operations)
assert result == expected, f"Test Case 1 failed. Expected: {expected}, Got: {result}"

# Test Case 2
state = [0, 1, 0, 1, 0, 1]
operations = ["L", "C(3)", "L", "C(0)", "L", "C(5)"]
expected = solution1(state[:], operations)
result = solution(state[:], operations)
assert result == expected, f"Test Case 2 failed. Expected: {expected}, Got: {result}"

# Test Case 3
state = [1, 0, 1, 0, 1]
operations = ["L", "C(1)", "L", "C(0)", "L"]
expected = solution1(state[:], operations)
result = solution(state[:], operations)
assert result == expected, f"Test Case 3 failed. Expected: {expected}, Got: {result}"

# Test Case 4
state = [0, 0, 0, 0, 0, 0]
operations = ["C(3)", "C(0)", "L", "L", "L", "C(4)"]
expected = solution1(state[:], operations)
result = solution(state[:], operations)
assert result == expected, f"Test Case 4 failed. Expected: {expected}, Got: {result}"

# Test Case 5
state = [1, 1, 1, 1, 1]
operations = ["L", "C(1)", "L", "C(0)", "L"]
expected = solution1(state[:], operations)
result = solution(state[:], operations)
assert result == expected, f"Test Case 5 failed. Expected: {expected}, Got: {result}"

# Test Case 6
state = [0, 0, 0, 0, 0]
operations = ["C(3)", "C(0)", "L", "L", "L", "C(4)"]
expected = solution1(state[:], operations)
result = solution(state[:], operations)
assert result == expected, f"Test Case 6 failed. Expected: {expected}, Got: {result}"

# Test Case 7
state = [1, 0, 1, 1, 1, 1]
operations = ["L", "L", "C(3)", "C(1)", "C(4)"]
expected = solution1(state[:], operations)
result = solution(state[:], operations)
assert result == expected, f"Test Case 7 failed. Expected: {expected}, Got: {result}"

# Test Case 8
state = [1, 0, 1, 0, 1, 0]
operations = ["L", "C(3)", "C(1)", "C(4)", "L", "L"]
expected = solution1(state[:], operations)
result = solution(state[:], operations)
assert result == expected, f"Test Case 8 failed. Expected: {expected}, Got: {result}"

# Test Case 9
state = [0, 1, 0, 1, 0, 1]
operations = ["L", "C(0)", "L", "C(2)", "L"]
expected = solution1(state[:], operations)
result = solution(state[:], operations)
assert result == expected, f"Test Case 9 failed. Expected: {expected}, Got: {result}"

# Test Case 10
state = [1, 0, 1, 0, 1, 0, 1, 0]
operations = ["L", "L", "C(3)", "C(1)", "C(6)", "L", "C(4)", "C(0)"]
expected = solution1(state[:], operations)
result = solution(state[:], operations)
assert result == expected, f"Test Case 10 failed. Expected: {expected}, Got: {result}"

print("All test cases passed successfully!")


