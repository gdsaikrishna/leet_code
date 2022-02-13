class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = max(map(lambda x: x[2], trips))
        ans = [0]*(n+1)
        for passengers,start,end in trips:
            ans[start] += passengers
            ans[end] -= passengers
            if passengers > capacity:
                return False
        res = ans[0]
        if res > capacity:
            return False
        for i in range(1,n+1):
            ans[i] += ans[i-1]
            res = max(ans[i], res)
            if res > capacity:
                return False
        return True