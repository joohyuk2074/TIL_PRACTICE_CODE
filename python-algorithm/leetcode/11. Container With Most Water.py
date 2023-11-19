class Solution(object):
    def maxArea(self, height):
        start = 0
        end = len(height) - 1

        answer = (end - start) * min(height[start], height[end])

        while start < end:
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
            area = (end - start) * min(height[start], height[end])
            answer = max(answer, area)

        return answer


solution = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
answer = solution.maxArea(height)
print(answer)

height1 = [2, 3, 4, 5, 18, 17, 6]
result1 = solution.maxArea(height1)
print(result1)
