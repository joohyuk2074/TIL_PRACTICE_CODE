class Solution(object):
    def recursive(self, n, memo):
        if n == 0 or n == 1:
            return 1

        if n not in memo:
            memo[n] = self.recursive(n - 1, memo) + self.recursive(n - 2, memo)

        return memo[n]

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        return self.recursive(n, memo)


stairs = Solution().climbStairs(4)
print(stairs)
