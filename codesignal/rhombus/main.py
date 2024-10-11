def solution(matrix, r):
    n, m = len(matrix), len(matrix[0])
    s = [[0] * (m - r - r + 2) for _ in range(n - r - r + 2)]
    # s[0][0] r - 1, r - 1
    for i in range(0, r << 1):
        for j in range(0, r << 1):
            if abs(i - (r - 1)) + abs(j - (r - 1)) + 1 <= r:
                s[0][0]+= matrix[i][j]
    # s[i][0]
    for i in range(1, (n - r - r + 2)):
        s[i][0] = s[i - 1][0]
        # r - 1 + i, r - 1
        # r - 1 + i - 1, r - 1
        for k in range(-(r - 1) , r):
            # 2 * r  -1 points
            s[i][0]-= matrix[r - 1 + i - (r - 1 - abs(k)) - 1][r - 1 + k]  
            s[i][0]+= matrix[r - 1 + i + (r - 1 - abs(k))][r - 1 + k]
    # s[i][j]
    for i in range(0, (n - r - r + 2)):
        for j in range(1, (m - r - r + 2)):
            s[i][j] = s[i][j - 1]
            # i + r - 1, j + r - 1
            cx = i + r - 1
            cy = j + r - 1
            for k in range(- (r - 1), r):
                s[i][j]-= matrix[cx + k][cy - (r - 1 - abs(k)) -1]
                s[i][j]+= matrix[cx + k][cy + (r - 1 - abs(k))]

    ans = -0x7f7f7f7f
    return ans

def solution1(matrix, r):
    n, m = len(matrix), len(matrix[0])
    s = [[0] * (m - r - r + 2) for _ in range(n - r - r + 2)]
    # s[0][0] r - 1, r - 1
    for i in range(0, r << 1):
        for j in range(0, r << 1):
            if abs(i - (r - 1)) + abs(j - (r - 1)) + 1 <= r:
                s[0][0]+= matrix[i][j]
    # s[i][0]
    for i in range(1, (n - r - r + 2)):
        s[i][0] = s[i - 1][0]
        # r - 1 + i, r - 1
        # r - 1 + i - 1, r - 1
        for k in range(-(r - 1) , r):
            # 2 * r  -1 points
            s[i][0]-= matrix[r - 1 + i - (r - 1 - abs(k)) - 1][r - 1 + k]  
            s[i][0]+= matrix[r - 1 + i + (r - 1 - abs(k))][r - 1 + k]
    # s[i][j]
    for i in range(0, (n - r - r + 2)):
        for j in range(1, (m - r - r + 2)):
            s[i][j] = s[i][j - 1]
            # i + r - 1, j + r - 1
            cx = i + r - 1
            cy = j + r - 1
            for k in range(- (r - 1), r):
                s[i][j]-= matrix[cx + k][cy - (r - 1 - abs(k)) -1]
                s[i][j]+= matrix[cx + k][cy + (r - 1 - abs(k))]

    ans = -0x7f7f7f7f
    return ans
matrix=[[0, 2, 4, 1, 6, 4],
[5, 1, 3, 4, 1, 5],
[0, 1, 2, 1, 2, 1],
[1, 3, 2, 1, 1, 2],
[4, 1, 3, 6, 5, 5],
[6, 7, 5, 3, 1, 2]]

for row in matrix:
    print(row)
radis = 3
expected = 35
result = solution(matrix, radis)
assert result == expected, f"Test Case 3 failed. Expected: {expected}, Got: {result}"