class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        def counter(arr):
            n = max(arr) + 1
            countArr = [0] * n
            for num in arr:
                countArr[num] += 1
            return countArr
        
        prefixSums = [x for x in accumulate(counter(nums))]
        result = []
        for num in nums:
            if num > 0:
                result.append(prefixSums[num-1])
            else:
                result.append(0)
       
        return result