class Solution(object):
    def __init__(self):
        self.answer = []

    def recursive(self, index, result, sum, target, candidates):
        if sum == target:
            self.answer.append(list(result))
            return

        if sum > target:
            return
        #
        # if index >= len(candidates):
        #     return

        for i in range(index, len(candidates)):
            result.append(candidates[i])
            self.recursive(i, result, sum + candidates[i], target, candidates)
            result.remove(candidates[i])

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        sorted_candidates = sorted(candidates)
        self.recursive(0, [], 0, target, sorted_candidates)

        return self.answer


solution = Solution()
candidates = [2, 3, 6, 7]
target = 7
result = solution.combinationSum(candidates, target)

print(result)
