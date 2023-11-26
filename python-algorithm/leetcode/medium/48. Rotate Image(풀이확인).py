class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        for i in range(row):
            for j in range(i + 1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for x in range(row):
            start_y = 0
            end_y = len(matrix) - 1

            while start_y <= end_y:
                temp = matrix[x][start_y]
                matrix[x][start_y] = matrix[x][end_y]
                matrix[x][end_y] = temp
                start_y += 1
                end_y -= 1

        print(matrix)


solution = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
solution.rotate(matrix)
