class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        multiple_result = 1
        for num in nums:
            multiple_result *= num

        answer = []
        if multiple_result != 0:
            for i in range(len(nums)):
                answer.append(multiple_result // nums[i])
        else:
            for i in range(len(nums)):
                if nums[i] != 0:
                    answer.append(0)
                else:
                    a = 1
                    for j in range(len(nums)):
                        if j != i:
                            a *= nums[j]
                    answer.append(a)

        return answer
