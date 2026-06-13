class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = defaultdict(int)
        for ch in t:
            d[ch] += 1

        formed, total = 0, len(d)
        sub_l, sub_r = 0,0
        l = r = 0
        len_ans = float('inf')
        while r < len(s):
            char = s[r]
            if char in d:
                d[char] -= 1
                if d[char] == 0:
                    formed += 1
            while l <= r and total == formed:
                cur_len = r - l + 1
                if cur_len < len_ans:
                    len_ans = cur_len
                    sub_l, sub_r = l,r + 1

                char = s[l]
                if char in d:
                    if d[char] == 0:
                        formed -= 1
                    d[char] += 1
                l += 1
            r += 1
        return "" if len_ans == float('inf') else s[sub_l: sub_r]







 
 
            
        