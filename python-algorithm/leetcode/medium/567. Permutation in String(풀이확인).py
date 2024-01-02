class Solution(object):
    def allDictZero(self, alpha_dict):
        for key in alpha_dict:
            if alpha_dict[key] != 0:
                return False

        return True

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        # s1 문자열의 dictionary 세팅 O(n)
        alpha_dict = {}
        for alpha in "abcdefghijklmnopqrstuvwxyz":
            alpha_dict[alpha] = 0

        for c in s1:
            alpha_dict[c] += 1

        for i in range(len(s2)):
            alpha_dict[s2[i]] -= 1
            if i - len(s1) >= 0:
                alpha_dict[s2[i - len(s1)]] += 1

            if self.allDictZero(alpha_dict):
                return True

        return False


solution = Solution()
inclusion = solution.checkInclusion("ab", "eidbaooo")
print(inclusion)
