class Solution(object):
    def isPalindrome(self, s):
        start_idx = 0
        end_idx = len(s) - 1

        while start_idx <= end_idx:
            if s[start_idx] != s[end_idx]:
                return False
            else:
                start_idx += 1
                end_idx -= 1

        return True

    def longestPalindrome(self, s):
        answer = ""
        max_length = 0

        for start_idx in range(0, len(s)):
            for end_idx in range(start_idx + 1, len(s) + 1):
                text = s[start_idx:end_idx]
                if self.isPalindrome(text):
                    if max_length < len(text):
                        max_length = len(text)
                        answer = text

        return answer


solution = Solution()
# palindrome = solution.longestPalindrome("babad")
# print(palindrome)

palindrome1 = solution.longestPalindrome("a")
print(palindrome1)
