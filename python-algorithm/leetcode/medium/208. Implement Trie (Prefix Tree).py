class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.word

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

input = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
value = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
