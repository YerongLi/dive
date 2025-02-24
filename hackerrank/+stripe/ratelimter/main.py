from collections import deque
import time

class RateLimiter:
    def __init__(self, max_requests, time_window):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = {}  # Dictionary to hold customer-specific request queues

    def allow_request(self, customer_id, weight=1):
        if weight > self.max_requests:  # If weight exceeds the limit, reject immediately
            return False

        current_time = time.time()
        
        # Initialize the customer's request deque if not already done
        if customer_id not in self.requests:
            self.requests[customer_id] = deque()

        # Remove outdated requests
        while self.requests[customer_id] and self.requests[customer_id][0][0] <= current_time - self.time_window:
            self.requests[customer_id].popleft()

        # Calculate the current weight of requests
        current_weight = sum(req[1] for req in self.requests[customer_id])

        # Check if new request can be allowed
        if current_weight + weight <= self.max_requests:
            self.requests[customer_id].append((current_time, weight))
            return True
        
        return False

# Testing the rate limiter
limiter = RateLimiter(5, 2)  # 2-second window, max 5 requests

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
assert limiter.allow_request(customer_id_1) == False  # Should fail, since current weight is at max (6)
print("Part 3 test passed: Request weight handling.")
