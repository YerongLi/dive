import time
from collections import *
class RateLimiter1:
    def __init__(self, limit, timelimit):
        self.limit = limit
        self.timelimit = timelimit
        self.q = deque()
        self.m = defaultdict(int)
    def allow_request(self, name):
        timestamp = time.time()
        while self.q and self.q[0][0] <= timestamp - self.timelimit:
            _, x = self.q.popleft()
            self.m[x]-= 1
        if self.m[name] == self.limit:
            return False
        self.m[name]+= 1
        self.q.append([timestamp, name])
        return True

class RateLimiter2:
    def __init__(self, limit, timelimit):
        self.limit = limit
        self.timelimit = timelimit
        self.q = deque()
        self.m = defaultdict(int)
    def allow_request(self, name):
        timestamp = time.time()
        while self.q and self.q[0][0] <= timestamp - self.timelimit:
            _, x = self.q.popleft()
            self.m[x]-= 1
        if self.m[name] == self.limit:
            return False
        self.m[name]+= 1
        self.q.append([timestamp, name])
        return True

class RateLimiter3:
    def __init__(self, limit, timelimit):
        self.limit = limit
        self.timelimit = timelimit
        self.q = deque()
        self.m = defaultdict(int)
    def allow_request(self, name, weight=1):
        timestamp = time.time()
        while self.q and self.q[0][0] <= timestamp - self.timelimit:
            _, x, ww = self.q.popleft()
            self.m[x]-= ww
        if self.m[name] + weight > self.limit:
            return False
        self.m[name]+= weight
        self.q.append([timestamp, name, weight])
        return True

# Testing the rate limiter
limiter = RateLimiter1(5, 2)  # 2-second window, max 5 requests

# Test 1: Basic request limit for one customer
customer_id_1 = "customer_1"
# Allow first 5 requests
for _ in range(5):
    assert limiter.allow_request(customer_id_1) == True

# 6th request should be rejected
assert limiter.allow_request(customer_id_1) == False

# Wait for 2 seconds so old requests expire
time.sleep(2)

# Now new requests should be allowed again
assert limiter.allow_request(customer_id_1) == True
print("Part 1 test passed: Basic request limit for one customer.")

# Test 2: Customer-specific rate limit
limiter = RateLimiter2(5, 2)
customer_id_2 = "customer_2"
# Allow first 5 requests for customer 2
for _ in range(5):
    assert limiter.allow_request(customer_id_2) == True

# 6th request for customer 2 should be rejected
assert limiter.allow_request(customer_id_2) == False

# Customer 1 should still be able to send requests
time.sleep(2)
assert limiter.allow_request(customer_id_1) == True
print("Part 2 test passed: Customer-specific rate limit.")

# Test 3: Request weight handling
# Define a heavy request that takes 2 weights
limiter = RateLimiter3(5, 2)
heavy_request_weight = 6  # This should be rejected since it's greater than max_requests
assert limiter.allow_request(customer_id_1, heavy_request_weight) == False

# Allow some regular requests
assert limiter.allow_request(customer_id_1) == True
assert limiter.allow_request(customer_id_1) == True

# Wait for 2 seconds so old requests expire
time.sleep(2)

# Now, we can allow a heavy request for customer 1
assert limiter.allow_request(customer_id_1, 4) == True  # Should succeed (2 weights remaining)
# Confirming the weight of requests after allowing a heavy request
assert limiter.allow_request(customer_id_1, 6) == False  # Should fail, since current weight is at max (6)
print("Part 3 test passed: Request weight handling.")
