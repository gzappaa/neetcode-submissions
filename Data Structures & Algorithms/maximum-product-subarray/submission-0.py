class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax = curmin = result = nums[0]


        for x in nums[1:]:
            candidates = (x, curmax * x, curmin * x)

            curmax = max(candidates)
            curmin = min(candidates)

            result = max(result, curmax)
        
        return result

        
        
        