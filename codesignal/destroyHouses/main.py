from re import X


def solution1(houses, queries):
   houses.sort()
   h = [0]
   seg = 0
   houseMap = {}
   prev = float("inf")
   for i in houses:
       if i-prev!=1:
           seg += 1
           # manually create a distance of 1 for non-contiguous houses
           h.append(0)
           h.append(1)
       else:
           h.append(1)
       houseMap[i] = len(h)-1
       prev = i
          
          
   # disjoint sets
   res = []
  
   for i in queries:
       houseInd = houseMap[i]
       if houseInd == 0:
           if h[1]==0:
               seg -= 1
       elif houseInd == len(h) - 1:
           if h[-2] == 0:
               seg -= 1
       else:
           if h[houseInd-1]==0 and h[houseInd+1]==0:
               seg -= 1
           elif h[houseInd-1]==1 and h[houseInd+1]==1:
               seg += 1
       h[houseInd] = 0
       res.append(seg)
   return res

def solution(houses, queries):
    ans = []
    pre = None
    houses.sort()
    res = 0
    m = {}
    a = []
    for h in houses:
        if h - 1 != pre: 
            res+= 1
            a.append(0)
        a.append(1)
        m[h] = len(a) - 1
        pre = h
    n = len(a)
    for q in queries:
        # 0 1 0  - 1
        # 0 1 1 
        # 1 1 0
        # 1 1 1  + 1
        pos = m[q]
        if (pos == 0 or a[pos - 1] == 0) and (pos== n -1 or a[pos+ 1] == 0):
            res-= 1
        elif pos > 0 and a[pos - 1] ==1 and pos < n and a[pos + 1] == 1:
            res+= 1
        a[pos] = 0
        ans.append(res)
    return ans

        
    return None

houses = [1,2,3,6,7,9]
queries = [6,3,7,2,9,1]
expected = solution1(houses, queries)
result = solution(houses, queries)

assert result == expected, f"Test Case 1 failed. Expected: {expected}, Got: {result}"
print('All test cases have passed!')


