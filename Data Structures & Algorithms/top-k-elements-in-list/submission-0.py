from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)

        # build frequency map
        for n in nums:
            counter[n] += 1

        # sort by frequency
        sorted_keys = sorted(counter, key=counter.get, reverse=True)

        return sorted_keys[:k]