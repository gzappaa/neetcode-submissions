class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def h_works(k):
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k
            return hours <= h

        l = 1
        r = max(piles)

        while l < r:
            k = (l + r) // 2
            if h_works(k):
                r = k
            else:
                l = k + 1

        return r


        