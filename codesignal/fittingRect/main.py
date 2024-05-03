
def solution1(operations):
    # 初始化一个存储0的位置的列表
    a = float("inf")
    b = float("inf")
    res = []
    for op in operations:
        curA = op[1]
        curB = op[2]
        if op[0] == 0:
            areaA = min(a, curA)*min(b, curB)
            areaB = min(a, curB)*min(b, curA)
            if areaA>areaB:
                a = min(a, curA)  
                b = min(b, curB)
            else:
                a = min(a, curB)
                b = min(b, curA)
        if op[0] == 1:
            if (curA<=a and curB<=b) or (curB<=a and curA<=b):
                res.append(True)
            else:
                res.append(False)
    return res




def solution(operations):
    a, b = 0x7f7f7f7f, 0x7f7f7f7f
    ans = []
    for o in operations:
        t, A, B = o
        if t == 0:
            area = min(A, a) * min(B, b)
            areaT = min(A, b) * min(B, a)
            if area < areaT: a, b = min(A, a), min(B, b)
            else: a, b = min(A, b), min(B, a)
        else:
            ans.append((A <= a and B<= b) or (B <= a and A <= b))
    return ans
# Test Case 1
operations = [[0, 3, 3], [0, 5, 2], [1, 3, 2], [1,2, 4]]
expected = solution1( operations)
result = solution(operations)
assert result == expected, f"Test Case 1 failed. Expected: {expected}, Got: {result}"
print('All test cases Passed')