class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dictionary = set()

        current_str = ""
        for c in s:
            if c not in current_str:
                current_str += c
            else:
                index = current_str.index(c)
                current_str = current_str[index + 1:] + c

            if current_str not in dictionary:
                dictionary.add(current_str)

        answer = 0
        for s in dictionary:
            if len(s) != 0:
                answer = max(answer, len(s))
        return answer


solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))
print(solution.lengthOfLongestSubstring(""))
print(solution.lengthOfLongestSubstring("dvdf"))
