class Solution:
    def __init__(self):
        self.res = []
        self.track = []
        self.used = []

    def permute(self, nums):
        self.used = [False] * len(nums)
        self.backtracking(nums)
        return self.res

    def backtracking(self, nums):
        if len(self.track) == len(nums):
            self.res.append(self.track.copy())
            return

        for i in range(len(nums)):
            if self.used[i]:
                continue
            self.track.append(nums[i])
            self.used[i] = True
            self.backtracking(nums)
            self.used[i] = False
            self.track.pop()


solution = Solution()
nums = [1, 2, 3]
print(solution.permute(nums))
