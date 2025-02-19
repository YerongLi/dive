import time
import heapq
from threading import Thread, Lock

def shorten_part(part):
    if len(part) <= 2:
        return part
    return f"{part[0]}{len(part) - 2}{part[-1]}"

def compress_url(url, m=None, t=None):
    def compress(part):
        if len(part) <= 2: return part
        return f'{part[0]}{len(part)-2}{part[-1]}'

    l = url.split('/')
    ans = []
    for x in l:
        parts = x.split('.')
        ans.append('.'.join([compress(p) for p in parts]))
    return '/'.join(ans)

# Test cases
def test_compress_url():
    assert compress_url("stripe.com/payments/checkout/customer.john.doe") == "s4e.c1m/p6s/c6t/c6r.j2n.d1e"
    assert compress_url("www.api.stripe.com/checkout") == "w1w.a1i.s4e.c1m/c6t"
    print('Passed part 1')
    assert compress_url("stripe.com/payments/checkout/customer.john.doe", m=2) == "s4e.c1m/p6s/c6t/c6r.j5e"
    assert compress_url("www.api.stripe.com/checkout", m=3) == "w1w.a1i.s7m/c6t"
    assert compress_url("stripe.com/payments/checkout/customer.john.doe", m=2, t=5) == "s4e.c1m/p6s/c6t/c6r.j5e"
    print("All test cases passed!")

test_compress_url()

