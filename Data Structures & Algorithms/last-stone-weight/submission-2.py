class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]
        while len(stones) > 1:
            heapq.heapify(stones)
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones,first - second)
        stones.append(0)
        return abs(stones[0]) 
