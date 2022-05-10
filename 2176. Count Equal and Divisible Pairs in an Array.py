class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        counter = {}
        for i in range(len(nums)):
            if nums[i] in counter:
                counter[nums[i]].append(i)
            else:
                counter[nums[i]]= [i]

        ans = 0
        for key, val in counter.items():
            length = len(val)
            for i in range(length-1):
                for j in range(i+1, length):
                    if val[i] * val[j] % k == 0:
                        ans += 1
        return ans