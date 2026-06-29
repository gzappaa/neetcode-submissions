class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]


        def simplerob(houses):
            if len(houses) == 1:
                return houses[0]


            houses[1] = max(houses[0], houses[1])

            for i in range(2, len(houses)):
                houses[i] = max(houses[i - 1], houses[i - 2] + houses[i])

            return houses[-1]

        return max(simplerob(nums[:-1]),simplerob(nums[1:]))
        