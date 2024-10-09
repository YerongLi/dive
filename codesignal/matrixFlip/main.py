def solution(matrix, q):
    n = len(matrix)
    if q == 0:
        # i, j = j, n - 1 - i
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            for j in range( (1+n) >> 1):
                matrix[i][j], matrix[i][n- 1- j] = matrix[i][n - 1 - j], matrix[i][j]
    
    if q == 1:
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    if q == 2:
        # i j -> n - 1 - j , n - 1 - i
        for i in range(n):
            for j in range(n - i):
                matrix[i][j], matrix[n - 1 - j][n - 1- i] = matrix[n - 1- j][n - 1- i], matrix[i][j]

    return matrix
def solution1(matrix, q):
    n = len(matrix)
    
    if q == 0:  # Rotate the matrix clockwise 90 degrees in place
        # Transpose the matrix
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse each row
        for i in range(n):
            matrix[i].reverse()
        
    elif q == 1:  # Flip the matrix on the main diagonal in place
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
    elif q == 2:  # Flip the matrix on the second diagonal in place
        for i in range(n):
            for j in range(n-i-1):
                matrix[i][j], matrix[n-j-1][n-i-1] = matrix[n-j-1][n-i-1], matrix[i][j]
        
        # If n is odd, swap the middle row and column elements
        if n % 2 != 0:
            mid = n // 2
            matrix[mid][mid], matrix[mid][mid] = matrix[mid][mid], matrix[mid][mid]
    
    else:
        return "Invalid query q"

    return matrix



matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

q = 0
assert solution(matrix, q) == solution1(matrix, q), f"Test failed for q = {q}"

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

q = 1
assert solution(matrix, q) == solution1(matrix, q), f"Test failed for q = {q}"

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

q = 2
assert solution(matrix, q) == solution1(matrix, q), f"Test failed for q = {q}"


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
for row in solution(matrix,2):
    print(row)
print("All tests passed!")