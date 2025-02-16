import time
import heapq
from threading import Thread, Lock

class LoadBalancer:
    def __init__(self, servers):
        self.servers = {server: 0 for server in servers}  # Server load mapping
        self.lock = Lock()
    
    def route(self, weight, process_time=None):
        with self.lock:
            # Find the server with the least load (tie-breaking by name order)
            sorted_servers = sorted(self.servers.items(), key=lambda x: (x[1], x[0]))
            server = sorted_servers[0][0]
            self.servers[server] += weight
        
        # If processing time is given, simulate processing asynchronously
        if process_time:
            Thread(target=self._process_request, args=(server, weight, process_time)).start()
        
        return server
    
    def _process_request(self, server, weight, process_time):
        time.sleep(process_time)  # Simulate processing time
        with self.lock:
            self.servers[server] -= weight

# Test cases
def test_load_balancer():
    lb = LoadBalancer(["a", "b", "c"])
    assert lb.route(1) == "a"  # "a" gets 1 load
    assert lb.route(1) == "b"  # "b" gets 1 load
    assert lb.route(1) == "c"  # "c" gets 1 load
    assert lb.route(1) == "a"  # "a" again since all equal
    print("Test case 1 passed")

def test_load_balancer_with_processing():
    lb = LoadBalancer(["a", "b", "c"])
    assert lb.route(2, 0.1) == "a"  # "a" gets 2 load
    assert lb.route(1, 0.3) == "b"  # "b" gets 1 load
    time.sleep(0.1)  # Wait for "a" to finish processing
    assert lb.route(2, 0.1) == "a"  # "a" should be available again
    print("Test case 2 passed")

test_load_balancer()
test_load_balancer_with_processing()

