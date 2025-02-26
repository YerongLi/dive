import time
from heapq import *
class LoadBalancer:
    def __init__(self, servers, max_load = 100):
        self.m = {x : 0 for x in servers}
        servers.sort()
        self.q = [[0, x] for x in servers]
        self.tq = [] # end time , name , cost
        self.max_load = max_load
    def route(self, cost):
        load, name = heappop(self.q)
        heappush(self.q, [load+cost, name])
        return name
    def route2(self, cost, ttl):
        timestamp = time.time()
        while self.tq and timestamp >= self.tq[0][0]:
            _, name, cc = heappop(self.tq)
            self.m[name]-= cc
            heappush(self.q, [self.m[name], name])

        while self.q and self.m[self.q[0][1]] != self.q[0][0]:
            heappop(self.q) # invalid
        load, name = heappop(self.q)
        self.m[name]+= cost
        heappush(self.tq, [timestamp+ttl, name, cost])
        heappush(self.q, [self.m[name], name])
        return name
    def route3(self, cost, ttl):
        timestamp = time.time()
        while self.tq and timestamp >= self.tq[0][0]:
            _, name, cc = heappop(self.tq)
            self.m[name]-= cc
            heappush(self.q, [self.m[name], name])

        while self.q and self.m[self.q[0][1]] != self.q[0][0]:
            heappop(self.q) # invalid
        load, name = heappop(self.q)
        if self.max_load < self.m[name] + cost: return None
        self.m[name]+= cost
        heappush(self.tq, [timestamp+ttl, name, cost])
        heappush(self.q, [self.m[name], name])
        return name

def test_load_balancer():
    lb = LoadBalancer(["a", "b", "c"])
    assert lb.route(1) == "a"  # "a" gets 1 load
    assert lb.route(1) == "b"  # "b" gets 1 load
    assert lb.route(1) == "c"  # "c" gets 1 load
    assert lb.route(1) == "a"  # "a" again since all equal
    print("Test case 1 passed")

def test_load_balancer_with_processing():
    lb = LoadBalancer(["a", "b", "c"])
    assert lb.route2(2, 0.1) == "a"  # "a" gets 2 load
    assert lb.route2(1, 0.3) == "b"  # "b" gets 1 load
    time.sleep(0.1)  # Wait for "a" to finish processing
    assert lb.route2(2, 0.1) == "a"  # "a" should be available again
    print("Test case 2 passed")

def test_load_balancer_with_max():
    lb = LoadBalancer(["a", "b", "c"], max_load=3)
    assert lb.route3(2, 0.2) == "a"  # "a" gets 2 load
    assert lb.route3(2, 0.2) == "b"  # "b" gets 2 load
    assert lb.route3(2, 0.2) == "c"  # "c" gets 2 load
    assert lb.route3(2, 0.2) is None  # No server can take 2 more load
    time.sleep(0.2)  # Wait for tasks to expire
    assert lb.route3(2, 0.2) == "a"  # "a" should be available again
    print("Test case 3 passed")
test_load_balancer()
test_load_balancer_with_processing()
test_load_balancer_with_max()


