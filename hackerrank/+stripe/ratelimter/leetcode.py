# Input
# ["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
# [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
# Output
# [null, true, true, false, false, false, true]

# Explanation
# Logger logger = new Logger();
# logger.shouldPrintMessage(1, "foo");  // return true, next allowed timestamp for "foo" is 1 + 10 = 11
# logger.shouldPrintMessage(2, "bar");  // return true, next allowed timestamp for "bar" is 2 + 10 = 12
# logger.shouldPrintMessage(3, "foo");  // 3 < 11, return false
# logger.shouldPrintMessage(8, "bar");  // 8 < 12, return false
# logger.shouldPrintMessage(10, "foo"); // 10 < 11, return false
# logger.shouldPrintMessage(11, "foo"); // 11 >= 11, return true, next allowed timestamp for "foo" is 11 + 10 = 21
from collections import *
class Logger:
    def __init__(self):
        self.q = deque()
        self.cache = set()
    
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self.q and self.q[0][0] <= timestamp - 10:
            t, m = self.q.popleft()
            self.cache.remove(m)
        ans = not (message in self.cache)
        if ans:
            self.q.append((timestamp, message))
            self.cache.add(message)
        return ans

# Instantiate Logger object and test the provided test case
logger = Logger()

# Test case input
test_case_inputs = [
    (1, "foo"), 
    (2, "bar"), 
    (3, "foo"), 
    (8, "bar"), 
    (10, "foo"), 
    (11, "foo")
]

# Expected outputs
expected_outputs = [
    True, 
    True, 
    False, 
    False, 
    False, 
    True
]

# Perform the tests and assert the results
for i, (timestamp, message) in enumerate(test_case_inputs):
    output = logger.shouldPrintMessage(timestamp, message)
    print(output)
    assert output == expected_outputs[i], f"Test failed at index {i}: expected {expected_outputs[i]}, got {output}"

print("All tests passed!")

