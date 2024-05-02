def solution1(binaryString, queries):
    n = len(binaryString)
    prefix_sum = [0] * (n + 1)
    flip = 0  # flip 初始为 0
    
    # 计算前缀和
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + (1 if binaryString[i - 1] == '0' else 0)
    
    ans = []
    for query in queries:

        if query == "flip":
            # 切换 flip 的值
            flip = 1 - flip
        else:
            query_type, index = query.split()
            index = int(index)
            # 根据 flip 的值返回结果
            if flip == 0:
                ans.append(prefix_sum[index])
            else:
                ans.append(index - prefix_sum[index])

            
    
    return ans

def solution(binaryString, queries):
    return None
# Test Case 1
binaryString = "101000"
queries = ["count 4", "flip", "count 1"]
expected = [3, 2]
result = solution(binaryString, queries)
assert result == expected, f"Test Case 1 failed. Expected: {expected}, Got: {result}"

# Test Case 2
binaryString = "10101111"
queries = ["count 4", "flip", "count 2"]
expected = [4, 2]
result = solution(binaryString, queries)
assert result == expected, f"Test Case 2 failed. Expected: {expected}, Got: {result}"

# Test Case 3
binaryString = "1100101"
queries = ["count 5", "flip", "flip", "count 6"]
expected = [4, 1, 5]
result = solution(binaryString, queries)
assert result == expected, f"Test Case 3 failed. Expected: {expected}, Got: {result}"

# Test Case 4
binaryString = "100100111"
queries = ["count 8", "flip", "count 2"]
expected = [5, 4]
result = solution(binaryString, queries)
assert result == expected, f"Test Case 4 failed. Expected: {expected}, Got: {result}"

# Test Case 5
binaryString = "110110011"
queries = ["count 4", "flip", "count 1", "flip", "count 9"]
expected = [3, 2, 5]
result = solution(binaryString, queries)
assert result == expected, f"Test Case 5 failed. Expected: {expected}, Got: {result}"

# Test Case 6
binaryString = "1110000"
queries = ["count 6", "flip", "flip", "flip", "count 3"]
expected = [0, 3, 4]
result = solution(binaryString, queries)
assert result == expected, f"Test Case 6 failed. Expected: {expected}, Got: {result}"

# Test Case 7
binaryString = "111111"
queries = ["count 6", "flip", "count 1"]
expected = [0, 5]
result = solution(binaryString, queries)
assert result == expected, f"Test Case 7 failed. Expected: {expected}, Got: {result}"

# Test Case 8
binaryString = "1010101010"
queries = ["count 9", "flip", "flip", "flip", "flip", "flip", "count 3"]
expected = [5, 4, 3]
result = solution(binaryString, queries)
assert result == expected, f"Test Case 8 failed. Expected: {expected}, Got: {result}"

# Test Case 9
binaryString = "100000000"
queries = ["count 9", "flip", "flip", "count 3"]
expected = [8, 1]
result = solution(binaryString, queries)
assert result == expected, f"Test Case 9 failed. Expected: {expected}, Got: {result}"

# Test Case 10
binaryString = "1111111"
queries = ["count 5", "flip", "count 1"]
expected = [0, 6]
result = solution(binaryString, queries)
assert result == expected, f"Test Case 10 failed. Expected: {expected}, Got: {result}"

print('All tests passed')