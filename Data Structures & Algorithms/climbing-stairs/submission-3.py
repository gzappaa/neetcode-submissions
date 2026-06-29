class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,2

        for i in range(n - 1):
            one, two = two, one + two

        return one
