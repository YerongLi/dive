def short(part):
    if len(part) <= 2:
        return part
    return f'{part[0]}{len(part)-2}{part[-1]}'

def part1(url):
    return '/'.join(['.'.join([short(part) for part in major.split('.')]) for major in url.split('/')])

def part2(url, m):
    compressed = []
    for major in url.split('/'):
        minors = major.split('.')
        if len(minors) > m:
            merged = ''.join(minors[m-1:])
            minors = minors[:m-1] + [merged]
        compressed.append('.'.join(short(part) for part in minors))
    return '/'.join(compressed)

def part3(url, m):
    minors = [minor for major in url.split('/') for minor in major.split('.')]
    if len(minors) > m:
        merged = ''.join(minors[m-1:])
        minors = minors[:m-1] + [merged]
    return '.'.join(short(part) for part in minors)

def run_tests():
    assert part1("stripe.com/payments/checkout/customer.john.doe") == "s4e.c1m/p6s/c6t/c6r.j2n.d1e"
    assert part1("www.api.stripe.com/checkout") == "w1w.a1i.s4e.c1m/c6t"
    
    assert part2("stripe.com/payments/checkout/customer.john.doe", 2) == "s4e.c1m/p6s/c6t/c6r.j5e"
    assert part2("www.api.stripe.com/checkout", 3) == "w1w.a1i.s7m/c6t"
    assert part2("com.stripe/user/access.someapi.endpoint", 2) == "c1m.s4e/u2r/a4s.s13t"
    
    assert part3("com.stripe/user/access.someapi.endpoint", 3) == "c1m.s4e.u23t"
    assert part3("stripe.com/payments/checkout/customer.john.doe", 3) == "s4e.c1m.p19e"
    
    print("All test cases passed!")

run_tests()

