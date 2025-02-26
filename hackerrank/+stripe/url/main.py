def short(part):
    if len(part) <= 2: return part
    return f'{part[0]}{len(part)-2}{part[-1]}'

def part1(url):
    l = [x.split('.') for x in url.split('/')]
    ans = []
    for x in l:
        ans.append('.'.join([short(part) for part in x]))
    res = '/'.join(ans)
    return res
def part2(url, m):
    l = [x.split('.') for x in url.split('/')]
    ans = []
    for x in l:
        if len(x) > m:
            x = x[:m-1] + [''.join(x[m-1:])]
        ans.append('.'.join([short(part) for part in x]))
    res = '/'.join(ans)
    return res

def part3(url, m):
    l = [x.split('.') for x in url.split('/')]
    ans = []
    length = [len(x) for x in l]
    if sum(length) > m:

        b, acc = 0,0
        while b  < len(length):
            acc+= length[b]
            if acc >= m - 1: break
        k = length[b]
        r = acc - (m - 1)
        merge = []
        for i in range(b+1, len(l)):
            merge+= l[i]
        if r:
            # split the l[b]
            merge = l[b][k-r:] + merge
            l[b] = l[b][:k-r] + [[''.join(merge)]]
            l = l[:b+1]
        else:
            l = l[:b+1] + [[''.join(merge)]]
    for x in l:
        ans.append('.'.join([short(part) for part in x]))
    res = '/'.join(ans)
    return res
def run_tests():
    assert part1("stripe.com/payments/checkout/customer.john.doe") == "s4e.c1m/p6s/c6t/c6r.j2n.d1e"
    assert part1("www.api.stripe.com/checkout") == "w1w.a1i.s4e.c1m/c6t"
    
    assert part2("stripe.com/payments/checkout/customer.john.doe", 2) == "s4e.c1m/p6s/c6t/c6r.j5e"
    assert part2("www.api.stripe.com/checkout", 3) == "w1w.a1i.s7m/c6t"
    assert part2("com.stripe/user/access.someapi.endpoint", 2) == "c1m.s4e/u2r/a4s.s13t"
    
    assert part3("com.stripe/user/access.someapi.endpoint", 3) == "c1m.s4e/u23t"
    assert part3("stripe.com/payments/checkout/customer.john.doe", 3) == "s4e.c1m/p29e"
    
    print("All test cases passed!")

run_tests()

