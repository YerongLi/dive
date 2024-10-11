def solution1(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # 创建四个方向的矩阵，初始值为0
    d1 = [[0] * cols for _ in range(rows)]  # 左上
    d2 = [[0] * cols for _ in range(rows)]  # 右上
    d3 = [[0] * cols for _ in range(rows)]  # 左下
    d4 = [[0] * cols for _ in range(rows)]  # 右下

    # 计算左上 (d1) 和 右上 (d2)
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                if i > 0 and j > 0:
                    d1[i][j] = d1[i-1][j-1] + 1
                else:
                    d1[i][j] = 1
                
                if i > 0 and j < cols - 1:
                    d2[i][j] = d2[i-1][j+1] + 1
                else:
                    d2[i][j] = 1

    # 计算左下 (d3) 和 右下 (d4)
    for i in range(rows-1, -1, -1):
        for j in range(cols):
            if matrix[i][j] == 1:
                if i < rows - 1 and j > 0:
                    d3[i][j] = d3[i+1][j-1] + 1
                else:
                    d3[i][j] = 1
                
                if i < rows - 1 and j < cols - 1:
                    d4[i][j] = d4[i+1][j+1] + 1
                else:
                    d4[i][j] = 1

    # 记录最大 X 形状的大小和中心坐标
    max_size = 0
    best_center = None

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                # 计算以 (i, j) 为中心的 X 形状的大小
                size = min(d1[i][j], d2[i][j], d3[i][j], d4[i][j])
                if size > max_size:
                    max_size = size
                    best_center = (i, j)

    return [best_center[0], best_center[1]] if best_center else []

# 示例输入
matrix = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]

# 输出结果
expected = [1, 1]  # 以 (1, 1) 为中心的最大 “X 形状”

assert solution1(matrix) == expected, f"Test Case 1 Failed: Expected {expected}, Got {solution1(matrix)}"


matrix = [
    [1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0]
]

# 输出结果
expected = [2, 2]  # 以 (2, 2) 为中心的最大 “X 形状”
assert solution1(matrix) == expected, f"Test Case Failed: Expected {expected}, Got {solution1(matrix)}"

matrix = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1]
]

# 输出结果
expected = [0, 0]  # 以 (2, 2) 为中心的最大 “X 形状”
assert solution1(matrix) == expected, f"Test Case 7 Failed: Expected {expected}, Got {solution1(matrix)}"