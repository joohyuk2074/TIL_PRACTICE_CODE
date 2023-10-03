class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [0] * (n + 1)

        def recursive(depth):
            if depth == 0 or depth == 1:
                return 0

            if dp[depth] != 0:
                return dp[depth]

            result1 = recursive(depth - 1) + cost[depth - 1]
            result2 = recursive(depth - 2) + cost[depth - 2]
            dp[depth] = min(result1, result2)

            return dp[depth]

        recursive(n)

        return dp[n]


solution = Solution()

cost1 = [10, 15, 20]
print(solution.minCostClimbingStairs(cost1))

cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(solution.minCostClimbingStairs(cost2))
