class Solution(object):
    def dp(self, i, s, st):
        if i >= len(s):
            self.lst.append(tuple(st))
            return
        for j in range(i, len(s)):
            if s[i:j + 1] == ''.join((reversed(s[i + j + 1]))):
                st.append(s[i:j + 1])
                x = self.dp(j + 1, s, st)
                st.pop()
        return

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.lst = []
        self.dp(0, s, [])
        return self.lst
