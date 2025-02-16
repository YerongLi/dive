from collections import deque
import time

class RateLimiter:
    def __init__(self, max_requests, time_window):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = deque()
    
    def allow_request(self):
        current_time = time.time()
        while self.requests and self.requests[0] <= current_time - self.time_window:
            self.requests.popleft()
        
        if len(self.requests) < self.max_requests:
            self.requests.append(current_time)
            return True
        return False

# Testing the rate limiter
limiter = RateLimiter(5, 2)  # 2-second window, max 5 requests

# Allow first 5 requests
for _ in range(5):
    assert limiter.allow_request() == True

# 6th request should be rejected
assert limiter.allow_request() == False

# Wait for 2 seconds so old requests expire
time.sleep(2)

# Now new requests should be allowed again
assert limiter.allow_request() == True

