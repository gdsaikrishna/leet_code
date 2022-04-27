class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def dfs(x,A):
            if x in d:
                A.append(x)
                for y in d.pop(x):
                    dfs(y, A)
        d = defaultdict(list)
        for x,y in pairs:
            d[x].append(y)
            d[y].append(x)
        s = list(s) 
        while d:
            x = next(iter(d))
            A = []
            dfs(x,A)
            A = sorted(A)
            B = sorted([s[i] for i in A])
            for i,b in enumerate(B):
                s[A[i]] = b
        return ''.join(s)