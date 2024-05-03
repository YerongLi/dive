def eliminate_bubbles(bubble, operations):
    n, m = len(bubble), len(bubble[0])  # n rows, m cols

    def drop_bubbles():
        for col in range(m):
            empty_rows = [row for row in range(n) if bubble[row][col] == 0]
            filled_rows = [row for row in range(n) if bubble[row][col] != 0]
            for i, row in enumerate(empty_rows + filled_rows):
                if i < len(empty_rows):
                    bubble[row][col] = 0
                else:
                    bubble[row][col] = bubble[filled_rows[i-len(empty_rows)]][col]

    def check_and_eliminate(r, c):
        if bubble[r][c] == 0:
            return False  # Do nothing for empty cell

        value = bubble[r][c]
        to_eliminate = {(r, c)}
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and bubble[nr][nc] == value:
                to_eliminate.add((nr, nc))

        if len(to_eliminate) > 2:
            for er, ec in to_eliminate:
                bubble[er][ec] = 0
            return True
        return False

    for r, c in operations:
        if check_and_eliminate(r, c):
            drop_bubbles()

    return bubble

# Example
bubble = [
    [1, 2, 3],
    [1, 2, 4],
    [1, 2, 2]
]

operations = [
    [0, 1],
    [2, 1]
]

print(eliminate_bubbles(bubble, operations))

