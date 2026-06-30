class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        

        def palin(l: int, r:int):
            local = 0
            while r < len(s) and l >= 0 and s[r] == s[l]:
                local += 1
                l -= 1
                r += 1

            return local

        for i in range(len(s)):
            count += palin(i, i)
            count += palin(i, i + 1)

        return count
  



        