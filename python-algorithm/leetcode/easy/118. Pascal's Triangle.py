class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        result = [[0 for _ in range(numRows)] for _ in range(numRows)]
        result[0][0] = 1

        for i in range(1, numRows):
            for j in range(0, numRows):
                if j == 0:
                    result[i][j] = 1
                else:
                    result[i][j] = result[i - 1][j - 1] + result[i - 1][j]

        answer = [[element for element in subarray if element != 0] for subarray in result]
        return answer


solution = Solution()
print(solution.generate(5))
