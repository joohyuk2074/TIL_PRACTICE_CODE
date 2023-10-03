class Solution:
    def climbStairs(self, n):
        dict = {}

        def recursive(num):
            if num == 1 or num == 0:
                return 1

            if num in dict:
                return dict[num]

            dict[num] = recursive(num - 1) + recursive(num - 2)
            return dict[num]

        return recursive(n)


solution = Solution()
print(solution.climbStairs(3))
