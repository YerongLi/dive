def getMinCost(self, cost: List[int], pairCost: int, k: int) -> int:
  k2 = k << 1
  n = len(cost)
  ans = sum(cost[:n - min(k2, n)])
  l, r = n - min(k2, n), len(cost) - 1
  while r - l >= 0:
    if cost[l] + cost[r] > pairCost:
      ans += pairCost
      l+= 1
      r-= 1
    else:
      ans+= cost[l]
      l+= 1
  return ans
