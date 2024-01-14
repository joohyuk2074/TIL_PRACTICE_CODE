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

    def partition(self, left, right, nums):
        # 피벗 선생
        pivot = nums[right]

        # 작은 요소의 인덱스
        i = left - 1

        # 배열을 피벗기준으로 나눈다
        for j in range(left, right):
            target = nums[j]
            if target < pivot:
                i += 1
                temp = nums[j]
                nums[j] = target
                nums[i] = temp

        pivot_pos = i + 1
        temp = nums[right]
        nums[right] = nums[pivot_pos]
        nums[pivot_pos] = temp

        return pivot_pos

    def quickSort(self, left, right, nums):
        if left >= right:
            return

        pivot_pos = self.partition(left, right, nums)

        self.quickSort(left, pivot_pos - 1, nums)
        self.quickSort(pivot_pos + 1, right, nums)

    def qs(self, nums):
        self.quickSort(0, len(nums) - 1, nums)

    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        self.qs(nums)

        return nums


solution = Solution()
nums = [2, 0, 2, 1, 1, 0]
print(solution.qs(nums))
