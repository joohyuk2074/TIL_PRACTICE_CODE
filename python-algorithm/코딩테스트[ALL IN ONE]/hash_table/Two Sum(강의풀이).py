class Solution:
    def twoSum(self, nums, target):
        memo = {}
        for v in nums:
            memo[v] = True
        for v in nums:
            needed_number = target - v
            if needed_number in memo:
                return True

        return False


nums = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))
