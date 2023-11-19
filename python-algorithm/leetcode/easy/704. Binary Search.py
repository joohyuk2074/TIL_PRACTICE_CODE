class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        answer = -1

        start = 0
        end = len(nums) - 1

        while start <= end:
            target_idx = (start + end) // 2

            if nums[target_idx] == target:
                answer = target_idx
                break
            elif nums[target_idx] < target:
                start = target_idx + 1
            else:
                end = target_idx - 1

        return answer


solution = Solution()
nums = [-1, 0, 3, 5, 9, 12]
target = 9
search = solution.search(nums, target)
print(search)
