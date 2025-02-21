import time
from heapq import *
class LoadBalancer:
    def __init__(self, ss, max_load = 0x7f7f7f7f):
        self.m = {s : 0 for s in ss}
        self.q = sorted([(0, s) for s in ss])
        self.tq = []
    def route(self, cost):
        load, name = heappop(self.q)
        self.m[name]+= cost
        heappush(self.q, (self.m[name], name))
        return name
    def route2(self, cost, ttl):
        now = time.time()
        while self.tq and self.tq[0][0] <= now:
            _, name, weight = heappop(self.tq)
            self.m[name]-= weight
            heappush(self.q, (self.m[name], name))

        while self.q:
            load, name = heappop(self.q)
            if load == self.m[name]:

                self.m[name]+= cost
                heappush(self.q, (self.m[name], name))
                heappush(self.tq, (now+ttl, name, cost))
                break

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

test_load_balancer()
test_load_balancer_with_processing()

