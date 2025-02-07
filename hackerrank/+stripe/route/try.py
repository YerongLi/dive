from collections import *
def solve1(inputString, source, target, method):
    g = defaultdict(list)
    mg = defaultdict(list)
    cg = defaultdict(list)
    if inputString:
        for r in inputString.split(','):
            xx, vv, mm, cc = r.split(':')
            g[xx].append(vv)
            mg[xx].append(mm)
            cc = int(cc)
            cg[xx].append(cc)

    for i, v in enumerate(g[source]):
        if mg[source][i] == method and v == target: return cg[source][i]
    return 'Route not found'
def solve2(inputString, source, target):
    g = defaultdict(list)
    mg = defaultdict(list)
    cg = defaultdict(list)
    if inputString:
        for r in inputString.split(','):
            xx, vv, mm, cc = r.split(':')
            g[xx].append(vv)
            mg[xx].append(mm)
            cc = int(cc)
            cg[xx].append(cc)

    p = defaultdict()
    reach = defaultdict()
    ans = inf = 0x7f7f7f7f
    res = None
    def dfs(x, step, cost):
        nonlocal ans, res
        if step == 3: return
        if x == target and cost < ans:
            ans = cost
            route = []
            method = []
            while x != source:
                route.append(x)
                method.append(reach[x])
                x = p[x]
            route.append(source)
            if len(method) == 2 and method[0] == method[1]: method.pop()

            res = {'cost': cost, 'route' : ' -> '.join(route[::-1]), 'method': ' -> '.join(method[::-1])}
            return 
        for i, v in enumerate(g[x]):
            newcost = cg[x][i] + cost
            p[v] = x
            reach[v] = mg[x][i]
            dfs(v, step + 1, newcost)
    dfs(source, 0, 0)
    if ans != inf: return res
    return 'Route not found'
        

def solve3(inputString, source, target):
    g = defaultdict(list)
    mg = defaultdict(list)
    cg = defaultdict(list)
    if inputString:
        for r in inputString.split(','):
            xx, vv, mm, cc = r.split(':')
            g[xx].append(vv)
            mg[xx].append(mm)
            cc = int(cc)
            cg[xx].append(cc)

    p = defaultdict()
    reach = defaultdict()
    ans = inf = 0x7f7f7f7f
    res = None
    def dfs(x, step, cost):
        nonlocal ans, res
        if step == 3: return
        if x == target and cost < ans:
            ans = cost
            route = []
            method = []
            while x != source:
                route.append(x)
                method.append(reach[x])
                x = p[x]
            route.append(source)
            if len(method) == 2 and method[0] == method[1]: method.pop()

            res = {'cost': cost, 'route' : ' -> '.join(route[::-1]), 'method': ' -> '.join(method[::-1])}
            return 
        for i, v in enumerate(g[x]):
            newcost = cg[x][i] + cost
            p[v] = x
            reach[v] = mg[x][i]
            dfs(v, step + 1, newcost)
    dfs(source, 0, 0)
    if ans != inf: return res
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