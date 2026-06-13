class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k
        res = []

        while r < len(nums) + 1:
            res.append(max(nums[l:r]))
            l += 1
            r += 1

        return res
