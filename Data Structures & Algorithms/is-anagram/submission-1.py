class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        word1 = {}
        word2 = {}

        for ch in s:
            word1[ch] = word1.get(ch, 0) + 1

        for ch in t:
            word2[ch] = word2.get(ch, 0) + 1

        return word1 == word2

      