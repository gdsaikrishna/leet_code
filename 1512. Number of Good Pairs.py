class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for i in nums:
            dic[i] +=1
        ans = 0
        for key in dic:
            ans+= (dic[key]*(dic[key]-1))//2
        return ans