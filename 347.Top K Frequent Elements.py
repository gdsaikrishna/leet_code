class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        heap = []
        for key in freq:
            if len(heap) == k:  
                heappushpop(heap,(freq[key],key))
            else:
                heappush(heap,(freq[key],key))
        res = []
        while k >0:
            k-=1
            res.append(heappop(heap)[1])
        return res