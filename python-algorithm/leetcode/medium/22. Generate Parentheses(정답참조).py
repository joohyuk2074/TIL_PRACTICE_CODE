class Solution(object):

    def generateParenthesis(self, n):
        def recursive(left, right, result):
            if len(result) == 2 * n:
                answer.append(result)
                return

            if left > n or right > n:
                return

            if left < n:
                recursive(left + 1, right, result + '(')

            if right < left:
                recursive(left, right + 1, result + ')')

        answer = []
        recursive(0, 0, '')
        return answer


solution = Solution()
n = 3
result = solution.generateParenthesis(n)
print(result)
