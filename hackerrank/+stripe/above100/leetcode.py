
from collections import defaultdict
from typing import List

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        m = defaultdict(int)
        for a, b, x in transactions:
            m[a]-= x
            m[b]+= x
        print(m)

        l = list()
        for name, x in m.items():
            l.append([name, x])
        n = len(l)
        ans = 0x7f7ff7f

        def dfs(i, step):
            # up till i -1 is fine >= 0
            nonlocal ans
            if step == ans: return
            p = i # next i
            while p < n:
                if l[p][1] < 0: break
                p+=1
            if p == n: 
                ans = step
                return
            for q in range(n): 
                if l[q][1] > 0:
                    x = min(-l[p][1], l[q][1])
                    l[p][1]+= x
                    l[q][1]-= x
                    dfs(p, step + 1)
                    l[p][1]-= x
                    l[q][1]+= x

            return ans
        dfs(0, 0)
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

