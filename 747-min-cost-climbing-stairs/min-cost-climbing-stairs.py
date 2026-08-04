class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for x in range(len(cost)-3, -1,-1):
            cost[x] = min(cost[x]+cost[x+1], cost[x]+cost[x+2])
        return min(cost[0], cost[1])