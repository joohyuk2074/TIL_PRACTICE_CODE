class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [0] * (n + 1)
        dp[1] = 0

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[n]


solution = Solution()

cost1 = [10, 15, 20]
print(solution.minCostClimbingStairs(cost1))

cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(solution.minCostClimbingStairs(cost2))
