# Constants for the size of the Trie
N = 2000      # Max number of nodes we need (adjust if needed)
M = N * 27      # Each node can have 26 children (for each letter) + 1 for end

# Global variables for the Trie and the counts
tr = [[0] * 26 for _ in range(M)]  # Trie structure (M x 26, for each letter)
cnt = [0] * M                      # Count of words ending at each Trie node
idx = 1                             # Trie node index

# Insert a word into the Trie in reverse order
def insert(word):
    global idx
    p = 0  # Start at the root of the Trie
    for i in range(len(word) - 1, -1, -1):  # Insert in reverse order
        u = ord(word[i]) - ord('a')
        if not tr[p][u]:
            tr[p][u] = idx  # Create a new Trie node
            idx += 1
        p = tr[p][u]
    cnt[p] += 1  # Mark the end of a word and increase its count

# Search the Trie for suffixes of the word
def search(word):
    p = 0
    res = 0
    for i in range(len(word) - 1, -1, -1):  # Traverse the Trie in reverse
        u = ord(word[i]) - ord('a')
        if not tr[p][u]:
            return res  # If no further match, return the current result
        p = tr[p][u]
        res += cnt[p]  # Add the count of words ending at this node
    return res - 1  # Subtract 1 to exclude the word itself

# Function to count suffix pairs
def solution(words):
    global tr, cnt, idx
    M = (len(words)+3) * 100
    tr = [[0] * 26 for _ in range(M)]  # Reset the Trie
    cnt = [0] * M                      # Reset the count
    idx = 1                            # Reset the Trie node index
    word_count_map = {}                # To handle duplicate words
    total_pairs = 0

    # Insert all words into the Trie
    for word in words:
        insert(word)

    # Count the number of suffix matches for each word
    for word in words:
        total_pairs += search(word)

    # Handle duplicates: subtract over-counted pairs due to duplicates
    for word in words:
        word_count_map[word] = word_count_map.get(word, 0) + 1

    for word, count in word_count_map.items():
        if count > 1:
            total_pairs -= (count * (count - 1)) // 2

    return total_pairs

# Test the function
words = ['backdoor', 'door','back', 'or']
expected = 3
result = solution(words)
assert result == expected, f"Test Case 1 failed. Expected: {expected}, Got: {result}"


words = ['a', 'a','a', 'a']
expected = 6
result = solution(words)
assert result == expected, f"Test Case 1 failed. Expected: {expected}, Got: {result}"