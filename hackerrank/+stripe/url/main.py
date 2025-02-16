import time
import heapq
from threading import Thread, Lock

def shorten_part(part):
    if len(part) <= 2:
        return part
    return f"{part[0]}{len(part) - 2}{part[-1]}"

def compress_url(url, m=None, t=None):
    major_parts = url.split('/')
    compressed_major_parts = []
    total_minor_parts = 0
    
    for major in major_parts:
        minor_parts = major.split('.')
        compressed_minor_parts = [shorten_part(part) for part in minor_parts]
        
        if m:
            compressed_minor_parts = compressed_minor_parts[:m]
        compressed_major_parts.append('.'.join(compressed_minor_parts))
        total_minor_parts += len(compressed_minor_parts)
    
    if t:
        compressed_major_parts = '.'.join(compressed_major_parts).split('.')[:t]
        return '/'.join(compressed_major_parts)
    
    return '/'.join(compressed_major_parts)

# Test cases
def test_compress_url():
    assert compress_url("stripe.com/payments/checkout/customer.john.doe") == "s4e.c1m/p6s/c6t/c6r.j2n.d1e"
    assert compress_url("www.api.stripe.com/checkout") == "w1w.a1i.s4e.c1m/c6t"
    assert compress_url("stripe.com/payments/checkout/customer.john.doe", m=2) == "s4e.c1m/p6s/c6t/c6r.j5e"
    assert compress_url("www.api.stripe.com/checkout", m=3) == "w1w.a1i.s7m/c6t"
    assert compress_url("stripe.com/payments/checkout/customer.john.doe", m=2, t=5) == "s4e.c1m/p6s/c6t/c6r.j5e"
    print("All test cases passed!")

test_compress_url()

