class Solution(object):
    def __init__(self):
        self.answer = set()

    # O(n)
    def validate(self, result):
        stack = []

        for c in result:
            if c == "(":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                stack.pop()

        if len(stack) == 0:
            return True
        else:
            return False

    def recursive(self, result, checks, input):
        if len(result) == len(input):
            if self.validate(result):
                self.answer.add(result)
            return

        for i in range(len(input)):
            if checks[i] is False:
                checks[i] = True
                result += input[i]
                self.recursive(result, checks, input)
                result = result[:-1]
                checks[i] = False

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        input = ""
        for _ in range(n):
            input += "()"

        checks = [False] * len(input)
        self.recursive("", checks, input)

        return self.answer


solution = Solution()
parenthesis = solution.generateParenthesis(3)
print(parenthesis)
