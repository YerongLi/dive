def solution(matrix, frameSize):
    n = len(matrix)       # Number of rows
    m = len(matrix[0])    # Number of columns
    
    # The size of the s array that stores frame sums
    s_rows = n - frameSize + 1
    s_cols = m - frameSize + 1
    
    # Initialize the s matrix to store sums of the frames
    s = [[0 for _ in range(s_cols)] for _ in range(s_rows)]
    
    max_sum = float('-inf')  # To track the maximum sum of frames
    distinct_elements = set()  # To track distinct elements in frames with max sum

    # Iterate over all possible top-left corners (i, j) of the submatrix
    for i in range(s_rows):
        for j in range(s_cols):
            frame_sum = 0
            current_elements = set()

            # Calculate the sum of the frame for the submatrix starting at (i, j)
            
            # Top row of the frame
            for k in range(j, j + frameSize):
                frame_sum += matrix[i][k]
                current_elements.add(matrix[i][k])
            
            # Bottom row of the frame (if frameSize > 1)
            if frameSize > 1:
                for k in range(j, j + frameSize):
                    frame_sum += matrix[i + frameSize - 1][k]
                    current_elements.add(matrix[i + frameSize - 1][k])
            
            # Left column of the frame (excluding the top and bottom corners to avoid double counting)
            for k in range(i + 1, i + frameSize - 1):
                frame_sum += matrix[k][j]
                current_elements.add(matrix[k][j])
            
            # Right column of the frame (excluding the top and bottom corners to avoid double counting)
            for k in range(i + 1, i + frameSize - 1):
                frame_sum += matrix[k][j + frameSize - 1]
                current_elements.add(matrix[k][j + frameSize - 1])
            
            # Store the frame sum in s[i][j]
            s[i][j] = frame_sum

            # Check if we have a new maximum sum
            if frame_sum > max_sum:
                max_sum = frame_sum
                distinct_elements = current_elements  # Replace with the new set of elements
            elif frame_sum == max_sum:
                distinct_elements.update(current_elements)  # Add new elements if same max sum
    for row in s:
        print(row)     
    print(sum([8, 9, 2, 1, 3, 10, 9 ,1]))
    print(distinct_elements)
    # Return the sum of distinct elements from frames with maximum sum
    return max_sum # sum(distinct_elements)

matrix = [
    [9, 7, 8, 9, 2],
    [6, 9, 9, 6, 1],
    [4, 10, 1, 3, 10],
    [18, 2, 3, 9, 3],
    [4, 6, 8, 5, 21]
]
print(solution(matrix, 3))
