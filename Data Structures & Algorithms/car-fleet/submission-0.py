class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l = [[p, s] for p, s in zip(position, speed)]
        curtime = count = 0

        for p,s in sorted(l)[::-1]:
            c = ((target - p) / s)
            if curtime < c:
                curtime = c
                count += 1
        return count
        