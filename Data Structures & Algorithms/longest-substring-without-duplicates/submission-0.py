class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chs = set()
        l = 0
        seq = 0

        for r in range(len(s)):
            while s[r] in chs:
                chs.remove(s[l])
                l += 1
            
            chs.add(s[r])
            seq = max(seq, r - l + 1)

        return seq

