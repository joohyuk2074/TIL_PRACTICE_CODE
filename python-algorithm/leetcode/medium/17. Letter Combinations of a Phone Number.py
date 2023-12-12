class Solution(object):
    def __init__(self):
        self.answer = []

    def recursive(self, digits_index, result, digits, digit_to_alpha):
        if digits_index >= len(digits):
            self.answer.append(result)
            return

        for c in digit_to_alpha[int(digits[digits_index])]:
            self.recursive(digits_index + 1, result + c, digits, digit_to_alpha)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if len(digits) == 0:
            return self.answer

        digit_to_alpha = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }

        self.recursive(0, "", digits, digit_to_alpha)

        return self.answer


solution = Solution()
digits = "23"
print(solution.letterCombinations(digits))
