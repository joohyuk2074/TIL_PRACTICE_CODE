class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        answer = []

        s_map = {}
        for s in strs:
            sorted_str = ''.join(sorted(s))

            if sorted_str in s_map:
                s_map[sorted_str].append(s)
            else:
                s_map[sorted_str] = [s]

        for key in s_map:
            answer.append(s_map.get(key))

        return answer


solution = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(solution.groupAnagrams(strs))
