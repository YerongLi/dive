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
    if inputString:
        for x in inputString.split(','):
            ss, tt, mm, cc = x.split(':')
            cc = int(cc)
            g[ss].append(tt)
            mg[ss].append(mm)
            cg[ss].append(cc)
    p = {}
    reach = {}
    ans = None
    def dfs(x, i, cost):
        nonlocal ans
        if ans: return
        if i == 3: return
        if x == target:
            route = []
            method = []
            while x != source:
                route.append(x)
                method.append(reach[x])
                x = p[x]
            route.append(source)
            if len(method) == 2 and method[0] == method[1]:
                method = method[:1]
            ans = {'cost': cost, 'route': ' -> '.join(route[::-1]), 'method': ' -> '.join(method[::-1])}
        for i, v in enumerate(g[x]):
            reach[v] = mg[x][i]
            p[v] = x
            dfs(v, i + 1, cost + cg[x][i])

    dfs(source, 0, 0)
    if ans: return ans
    return 'Route not found'

def solve3(inputString, source, target):
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
    p = {}
    reach = {}
    ans = None
    def dfs(x, i, cost):
        nonlocal ans
        if i == 3: return
        if x == target:
            if not ans or ans['cost'] > cost:
                route = []
                method = []
                while x != source:
                    route.append(x)
                    method.append(reach[x])
                    x = p[x]
                route.append(source)
                if len(method) == 2 and method[0] == method[1]:
                    method = method[:1]
                ans = {'cost': cost, 'route' : ' -> '.join(route[::-1]), 'method': ' -> '.join(method[::-1])}
        for i, v in enumerate(g[x]):
            p[v] = x
            reach[v] = mg[x][i]
            dfs(v, i + 1, cost + cg[x][i])
    dfs(source, 0, 0)
    if ans: return ans

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