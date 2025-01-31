from collections import *
inf = 0x3f3f3f3f
def solve1(inputString, source, target, method):
    g = defaultdict(list)
    cg = defaultdict(list)
    mg = defaultdict(list)
    if inputString:
        for x in inputString.split(','):
            ss, tt, mm, cc = x.split(':')
            g[ss].append(tt)
            cg[ss].append(int(cc))
            mg[ss].append(mm)
    for i in range(len(g[source])):
        if g[source][i] == target and mg[source][i] == method:
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
    ans = 0x3f3f3f3f         
    for i in range(len(g[source])):
        if g[source][i] == target:
            ans = cg[source][i]
            method = mg[source][i]
            route = f'{source} -> {target}'
    if ans == 0x3f3f3f3f:

        targetm = {x : i for i, x in enumerate(rg[target])}
        for i, v in enumerate(g[source]):
            if v in targetm:
                j = targetm[v]
                method = mg[source][i] if rmg[target][j] == mg[source][i] else f'{mg[source][i]} -> {rmg[target][j]}' 
                route = f'{source} -> {v} -> {target}'
                ans = cg[source][i] + rcg[target][j]
    if ans != 0x3f3f3f3f:
        return {'cost' : ans, 'route': route, 'method': method}
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
    ans = 0x3f3f3f3f         
    for i in range(len(g[source])):
        if g[source][i] == target and cg[source][i] < ans:
            ans = cg[source][i]
            method = mg[source][i]
            route = f'{source} -> {target}'


    targetm = {x : i for i, x in enumerate(rg[target])}
    for i, v in enumerate(g[source]):
        if v in targetm:
            j = targetm[v]
            newcost = cg[source][i] + rcg[target][j]
            if newcost < ans:
                method = mg[source][i] if rmg[target][j] == mg[source][i] else f'{mg[source][i]} -> {rmg[target][j]}' 
                route = f'{source} -> {v} -> {target}'
                ans = newcost
    if ans != 0x3f3f3f3f:
        return {'cost' : ans, 'route': route, 'method': method}
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