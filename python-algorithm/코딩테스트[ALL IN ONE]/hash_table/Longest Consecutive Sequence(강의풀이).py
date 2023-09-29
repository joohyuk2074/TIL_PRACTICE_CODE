class Solution:
    def longestConsecutive(self, nums):
        longest = 0
        num_dict = {}
        for num in nums:
            num_dict[num] = True

        for num in num_dict:
            if num - 1 not in num_dict:
                cnt = 1
                target = num + 1
                while target in num_dict:
                    target += 1
                    cnt += 1
                longest = max(longest, cnt)

        return longest


solution = Solution()

nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(solution.longestConsecutive(nums))

nums1 = [1, 2, 0, 1]
print(solution.longestConsecutive(nums1))

num2 = [6, 7, 100, 5, 4, 4]
print(solution.longestConsecutive(num2))
