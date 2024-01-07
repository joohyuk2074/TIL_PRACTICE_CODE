class Solution:
    def bubbleSort(self, nums):
        for i in range(0, len(nums) - 1):
            for j in range(0, len(nums) - 1 - i):
                if nums[j] > nums[j + 1]:
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp

    def selectionSort(self, nums):
        for i in range(0, len(nums)):
            min_idx = i
            for j in range(i + 1, len(nums)):
                if nums[min_idx] > nums[j]:
                    min_idx = j

            temp = nums[i]
            nums[i] = nums[min_idx]
            nums[min_idx] = temp

    def insertionSort(self, nums):
        for i in range(1, len(nums)):  # target 인덱스
            key = nums[i]
            j = i - 1  # 비교 시작 인덱스
            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key

    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        self.insertionSort(nums)

        return nums


solution = Solution()
nums = [2, 0, 2, 1, 1, 0]
print(solution.sortColors(nums))
