from collections import defaultdict
def solve1(inputString, source, target, method):
    g = defaultdict(list)
    mg = defaultdict(list)
    cg = defaultdict(list)
    if inputString:
        for x in inputString.split(','):
            ss, tt, mm, cc = x.split(':')
            cc = int(cc)
            g[ss].append(tt)
            mg[ss].append(mm)
            cg[ss].append(cc)
    for i, v in enumerate(g[source]):
        if v == target and mg[source][i] == method:
            return cg[source][i]
    return 'Route not found'

def solve2(inputString, source, target):
    g = defaultdict(list)
    mg = defaultdict(list)
    cg = defaultdict(list)
    rg = defaultdict(list)
    rmg = defaultdict(list)
    rcg = defaultdict(list)
    
    if inputString:
        for x in inputString.split(','):
            ss, tt, mm, cc = x.split(':')
            cc = int(cc)
            g[ss].append(tt)
            mg[ss].append(mm)
            cg[ss].append(cc)

            rg[tt].append(ss)
            rmg[tt].append(mm)
            rcg[tt].append(cc)

    inf = 0x7f7f7f7f
    ans = inf
    for i, v in enumerate(g[source]):
        if v == target:
            ans = cg[source][i]
            method = mg[source][i]
            route = ' -> '.join([source, target])
    parents = defaultdict(list)
    for j, v in enumerate(rg[target]):
        parents[v].append(j)
    for i, v in enumerate(g[source]):
        for j in parents[v]:
            ans = cg[source][i] + rcg[target][j]
            method = mg[source][i] if mg[source][i] == rmg[target][j] else ' -> '.join([mg[source][i], rmg[target][j]])
            route = ' -> '.join([source, v, target])
    if ans != inf: return {'cost': ans, 'route': route, 'method': method}
    return 'Route not found'   

def solve3(inputString, source, target):
    g = defaultdict(list)
    mg = defaultdict(list)
    cg = defaultdict(list)
    rg = defaultdict(list)
    rmg = defaultdict(list)
    rcg = defaultdict(list)
    
    if inputString:
        for x in inputString.split(','):
            ss, tt, mm, cc = x.split(':')
            cc = int(cc)
            g[ss].append(tt)
            mg[ss].append(mm)
            cg[ss].append(cc)

            rg[tt].append(ss)
            rmg[tt].append(mm)
            rcg[tt].append(cc)

    inf = 0x7f7f7f7f
    ans = inf
    for i, v in enumerate(g[source]):
        if v == target:
            newcost = cg[source][i]
            if newcost >= ans: continue
            ans = newcost
            method = mg[source][i]
            route = ' -> '.join([source, target])
    parents = defaultdict(list)
    for j, v in enumerate(rg[target]):
        parents[v].append(j)
    for i, v in enumerate(g[source]):
        for j in parents[v]:

            newcost = cg[source][i] + rcg[target][j]
            if newcost >= ans: continue
            ans = newcost
            method = mg[source][i] if mg[source][i] == rmg[target][j] else ' -> '.join([mg[source][i], rmg[target][j]])
            route = ' -> '.join([source, v, target])
    if ans != inf: return {'cost': ans, 'route': route, 'method': method}
    return 'Route not found'
def test_solve1():
    inputString = "US:UK:UPS:4,US:UK:DHL:5,UK:CA:FedEx:10,AU:JP:DHL:20"
    
    # Direct route with UPS from US to UK, should return cost 4
    assert solve1(inputString, "US", "UK", "UPS") == 4
    
    # Direct route with DHL from US to UK, should return cost 5
    assert solve1(inputString, "US", "UK", "DHL") == 5
    
    # Route not found (invalid method)
    assert solve1(inputString, "US", "UK", "FedEx") == "Route not found"
    
    # Route not found (invalid countries)
    assert solve1(inputString, "AU", "UK", "UPS") == "Route not found"
    
    # Edge case with empty string input
    assert solve1("", "US", "UK", "UPS") == "Route not found"
    
def test_solve2():
    inputString = "US:UK:UPS:4,US:UK:DHL:5,UK:CA:FedEx:10,AU:JP:DHL:20"
    
    # Route from US -> UK -> CA
    result = solve2(inputString, "US", "CA")
    assert result in [{
        "route": "US -> UK -> CA",
        "method": "UPS -> FedEx",
        "cost": 14
    },
    {'cost': 15, 'route': 'US -> UK -> CA', 'method': 'DHL -> FedEx'}
    ]
    
    # Route from AU -> JP (direct, no intermediate)
    result = solve2(inputString, "AU", "JP")
    assert result in [{'cost': 20, 'route': 'AU -> JP', 'method': 'DHL'}
    ]
    
    # Edge case: empty string input
    result = solve2("", "US", "CA")
    assert result == "Route not found"

def test_solve3():
    inputString = "US:UK:UPS:4,US:UK:DHL:5,UK:CA:FedEx:10,AU:JP:DHL:20"
    
    # Route with minimum cost for US -> CA
    result = solve3(inputString, "US", "CA")
    assert result == {
        "route": "US -> UK -> CA",
        "method": "UPS -> FedEx",
        "cost": 14
    }
    
    # Case where no valid route exists
    result = solve3(inputString, "AU", "JP")
    assert result in [{'cost': 20, 'route': 'AU -> JP', 'method': 'DHL'}
    ]
    
    
    # Edge case: empty string input
    result = solve3("", "US", "CA")
    print(result)
    assert result == "Route not found"
test_solve1()
test_solve2()
test_solve3()

print("All tests passed!")