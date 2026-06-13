class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}
        window = {}
        for c in s1:
            need[c] = need.get(c, 0) + 1

        have, total = 0, len(need)

        l = 0
        for r, c in enumerate(s2):
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    have += 1

            if r - l + 1 == len(s1):
                if have == total:
                    return True
                left = s2[l]
                if left in need:
                    if window[left] == need[left]:
                        have -= 1
                    window[left] -= 1
                l += 1

        return False