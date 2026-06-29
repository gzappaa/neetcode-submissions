class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        reslen = 0

        #odd
        for i in range(len(s)):
            r, l = i,i
            while  l >= 0 and r < len(s) and s[r] == s[l]:
                if (r - l + 1) > reslen:
                    res = s[l: r + 1]
                    reslen = r - l + 1
                l -= 1
                r += 1


        for i in range(len(s)):
            r, l = i + 1,i
            while r < len(s) and l >= 0 and s[r] == s[l]:
                if (r - l + 1) > reslen:
                    res = s[l: r + 1]
                    reslen = (r - l + 1)
                l -= 1
                r += 1

        return res


        


        