class Solution:
    def twoSum(self, nums, target):
        answer = []
        dict = {}

        for i in range(len(nums)):
            number = nums[i]

            target_number = target - number
            if target_number in dict:
                answer.append(dict[target_number])
                answer.append(i)
            else:
                dict[number] = i

        answer.sort()
        return answer


nums = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))
