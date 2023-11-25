class Solution(object):

    def __init__(self):
        self.answer = []

    def recursive(self, index, cur_cnt, result, cnt, nums):
        if cur_cnt == cnt:
            self.answer.append(list(result))
            return

        if index >= len(nums):
            return

        result.append(nums[index])
        self.recursive(index + 1, cur_cnt + 1, result, cnt, nums)
        result.remove(nums[index])
        self.recursive(index + 1, cur_cnt, result, cnt, nums)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        for set_cnt in range(len(nums) + 1):
            self.recursive(0, 0, [], set_cnt, nums)

        return self.answer


nums = [1, 2, 3]
subsets = Solution().subsets(nums)
print(subsets)
