def solution(matrix, q):
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

# Example usage:
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

q = 0
print(solution(matrix, q))  # Rotate the matrix clockwise 90 degrees in place

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
q = 1
print(solution(matrix, q))  # Flip the matrix on the main diagonal in place

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
q = 2
print(solution(matrix, q))  # Flip the matrix on the second diagonal in place

