import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #get frequency and negate value since min heap by default
        count = {}
        for num in nums: # O(n)
            count[num] = count.get(num, 0) + 1

        #build a heap must flip order because heapify works on the first item in tuple
        max_heap = [(-value, key) for key, value in count.items()]
        heapq.heapify(max_heap) #O(logm)

        res = []
        while len(res) < k:
            value, key = heapq.heappop(max_heap)
            res.append(key)
        return res