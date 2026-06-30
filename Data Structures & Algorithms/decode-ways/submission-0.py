class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        
        n = len(s) + 1
        dp = n * [0]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(s) + 1):
            onedigit = s[i - 1]
            twodigit = s[i - 2:i]

            if onedigit != "0":
                dp[i] += dp[i-1]

            if "10" <= twodigit <= "26":
                dp[i] += dp[i - 2]

        return dp[-1]

        


            
        