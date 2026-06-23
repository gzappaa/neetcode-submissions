class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            largest = heapq.heappop(stones)
            sec_largest = heapq.heappop(stones)

            if largest != sec_largest:
                heapq.heappush(stones, largest - sec_largest)

        return -stones[0] if stones else 0

