def redistribute_funds(accounts):
    p, q = 0, 0
    l = [[name, a-100] for name, a in accounts.items()]
    n = len(l)
    ans = []
    while p < n:
        if l[p][1] < 0:
            while q < n:
                if l[q][1] > 0: break
                q+= 1
            x = min(abs(l[p][1]), abs(l[q][1]))
            l[p][1]+= x
            l[q][1]-= x
            f, t = l[q][0], l[p][0]
            ans.append({'from': f, 'to': t, 'amount': x})
        else:
            p+= 1
    if p <n and l[p][1] < 0: return None
    return ans

    

def min_redistribute_funds(accounts):
    l = [[name, a - 100] for name, a in accounts.items()]
    n = len(l)
    
    tmp = []
    ans = None
    def dfs(i):
        nonlocal ans, tmp
        if ans and len(tmp) == len(ans): return

        p = i
        while p < n:
            if l[p][1] < 0: break
            p+= 1
        if p == n:
            ans = [x for x in tmp]
            return 
        for q in range(n):
            if l[q][1] > 0:
                x = min(abs(l[p][1]), abs(l[q][1]))
                l[p][1]+= x
                l[q][1]-= x
                tmp.append({'from': l[q][0], 'to': l[p][0], 'amount': x})
                dfs(p)
                tmp.pop()
                l[p][1]-= x
                l[q][1]+= x
        return
    dfs(0)
    return ans