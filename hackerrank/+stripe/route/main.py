from collections import *
def solve1(inputString, source, target, method):
    g = defaultdict(list)
    mg = defaultdict(list)
    cg = defaultdict(list)
    if inputString:
        for l in inputString.split(','):
            xx, vv, mm, cc = l.split(':')
            cc = int(cc)
            g[xx].append(vv)
            mg[xx].append(mm)
            cg[xx].append(cc)
    for i, v in enumerate(g[source]):
        if mg[source][i] == method and v == target: return cg[source][i]
    return 'Route not found'

def solve2(inputString, source, target):
    g = defaultdict(list)
    mg = defaultdict(list)
    cg = defaultdict(list)

    rg = defaultdict(list)
    rmg = defaultdict(list)
    rcg = defaultdict(list)
    if inputString:
        for l in inputString.split(','):
            xx, vv, mm, cc = l.split(':')
            cc = int(cc)
            g[xx].append(vv)
            mg[xx].append(mm)
            cg[xx].append(cc)


            rg[vv].append(xx)
            rmg[vv].append(mm)
            rcg[vv].append(cc)

    inf = 0x3f3f3f3f
    ans = inf
    for i, v in enumerate(g[source]):
        if v == target: 
            ans = cg[source][i]
            method = mg[source][i]
            route = f'{source} -> {target}'
            break

    if ans == inf:
        parents = {v : j for j, v in enumerate(rg[target])}
        for i, v in enumerate(g[source]):
            if v in parents:
                j = parents[v]
                ans = cg[source][i] + rcg[target][j]
                method = mg[source][i] if mg[source][i] == rmg[target][j] else f'{mg[source][i]} -> {rmg[target][j]}' 
                route = ' -> '.join([source, v, target])
                break
    if ans != inf:
        return {'cost': ans, 'method': method, 'route': route}
    return 'Route not found'

def solve3(inputString, source, target):
    g = defaultdict(list)
    mg = defaultdict(list)
    cg = defaultdict(list)

    rg = defaultdict(list)
    rmg = defaultdict(list)
    rcg = defaultdict(list)
    if inputString:
        for l in inputString.split(','):
            xx, vv, mm, cc = l.split(':')
            cc = int(cc)
            g[xx].append(vv)
            mg[xx].append(mm)
            cg[xx].append(cc)


            rg[vv].append(xx)
            rmg[vv].append(mm)
            rcg[vv].append(cc)

    inf = 0x3f3f3f3f
    ans = inf
    for i, v in enumerate(g[source]):
        if v == target:
            newcost = cg[source][i]
            if newcost >= ans: continue
            ans = newcost
            method = mg[source][i]
            route = f'{source} -> {target}'

    if ans == inf:
        parents = {v : j for j, v in enumerate(rg[target])}
        for i, v in enumerate(g[source]):
            if v in parents:
                j = parents[v]
                newcost = cg[source][i] + rcg[target][j]
                if newcost >= ans: continue
                ans = newcost
                method = mg[source][i] if mg[source][i] == rmg[target][j] else f'{mg[source][i]} -> {rmg[target][j]}' 
                route = ' -> '.join([source, v, target])
    if ans != inf:
        return {'cost': ans, 'method': method, 'route': route}
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
    print(result)
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
    assert result == "Route not found"
test_solve1()
test_solve2()
test_solve3()

print("All tests passed!")