class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #Convert the List into -ve Numbers as Python does not contain Max Heap
        stones  = [ -s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first  = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if first < second:
                heapq.heappush(stones, first - second)
        stones.append(0)
        return abs(stones[0])
            