class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
        def is_good(i, j, k):
            ok_a = abs(arr[i] - arr[j]) <= a
            ok_b = abs(arr[j] - arr[k]) <= b
            ok_c = abs(arr[i] - arr[k]) <= c
            return all((ok_a, ok_b, ok_c))
        
        size = len(arr)
        ans = sum(1 for i in range(size-2) for j in range(i+1, size-1) for k in range(j+1, size) if is_good(i,j,k))
        return ans