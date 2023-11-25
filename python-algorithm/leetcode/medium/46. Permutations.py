class Solution(object):
    def __init__(self):
        self.answer = []

    def recursive(self, result, nums, check):
        if len(result) == len(nums):
            self.answer.append(list(result))
            return

        for i in range(len(nums)):
            if check[i] is False:
                result.append(nums[i])
                check[i] = True
                self.recursive(result, nums, check)
                check[i] = False
                result.remove(nums[i])

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        check = [False] * len(nums)

        self.recursive(result, nums, check)

        return self.answer


solution = Solution()

nums = [1, 2, 3]
permute = solution.permute(nums)
print(permute)
