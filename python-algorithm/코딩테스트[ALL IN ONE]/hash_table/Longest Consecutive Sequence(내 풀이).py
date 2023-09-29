class Solution:
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0

        nums_set = set(nums)
        new_nums = list(nums_set)
        new_nums.sort()

        answer = 0
        length = 1
        cur_number = new_nums[0]
        for i in range(1, len(new_nums)):
            if cur_number + 1 == new_nums[i]:
                cur_number = new_nums[i]
                length += 1
            else:
                if answer < length:
                    answer = length
                cur_number = new_nums[i]
                length = 1

        if answer < length:
            answer = length

        return answer


solution = Solution()

nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(solution.longestConsecutive(nums))

nums1 = [1, 2, 0, 1]
print(solution.longestConsecutive(nums1))

num2 = [6, 7, 100, 5, 4, 4]
print(solution.longestConsecutive(num2))
