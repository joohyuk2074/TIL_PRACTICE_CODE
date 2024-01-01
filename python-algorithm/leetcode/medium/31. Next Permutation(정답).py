class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        answer = []
        sorted_nums = sorted(nums)

        def recursive(visited, result):
            if len(result) >= len(nums):
                answer.append(list(result))
                return

            for i in range(len(nums)):
                if visited[i] is False:
                    visited[i] = True
                    result.append(sorted_nums[i])
                    recursive(visited, result)
                    result.pop()
                    visited[i] = False

        visited = [False] * len(nums)
        recursive(visited, result=[])

        index = answer.index(nums)
        if index == len(answer) - 1:
            nums = list(answer[0])
        else:
            nums = list(answer[index + 1])

        print(nums)


solution = Solution()
nums = [1, 2, 3]
permutation = solution.nextPermutation(nums)
print(permutation)
