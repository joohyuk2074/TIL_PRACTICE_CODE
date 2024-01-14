class Solution:
    def findDuplicate(self, nums):
        exists_set = set()

        for num in nums:
            if num in exists_set:
                return num
            else:
                exists_set.add(num)

        return 0


solution = Solution()
nums = [1, 3, 4, 2, 2]
duplicate = solution.findDuplicate(nums)
print(duplicate)
