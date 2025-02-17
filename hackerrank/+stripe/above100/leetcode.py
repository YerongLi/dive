
from collections import defaultdict
from typing import List

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        m = defaultdict(int)
        for a, b, x in transactions:
            m[a] -= x
            m[b] += x
        ans = 0x7f7f7f7f
        def dfs(step):
            nonlocal m, ans
            if step >= ans:
                return
            allzero = True
            for k in m:
                if m[k] != 0:
                    allzero = False
                    break
            if allzero:
                ans = step
                return

            keys = [(m[x], x) for x in m]
            keys.sort()
            for _, i in keys:
                if m[i] >= 0: continue
                for _, j in keys[::-1]:
                    if m[j] <= 0: continue
                    x = max(-m[i], m[j])
                    m[i] += x
                    m[j] -= x
                    dfs(step + 1)
                    m[i] -= x
                    m[j] += x
        dfs(0)
        return ans

# Instantiate the solution object
sol = Solution()

# Test case 1
transactions1 = [[0, 1, 10], [2, 0, 5]]
expected_output1 = 2
assert sol.minTransfers(transactions1) == expected_output1, f"Test case 1 failed: expected {expected_output1}, got {sol.minTransfers(transactions1)}"

# Test case 2
transactions2 = [[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]
expected_output2 = 1
assert sol.minTransfers(transactions2) == expected_output2, f"Test case 2 failed: expected {expected_output2}, got {sol.minTransfers(transactions2)}"

print("All test cases passed!")

