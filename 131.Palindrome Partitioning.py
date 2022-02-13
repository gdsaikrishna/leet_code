#Thanks StefanPochmann for this wonderful 1-liner
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return [[s[:i]] + rest
            for i in range(1, len(s)+1)
            if s[:i] == s[i-1::-1]
            for rest in self.partition(s[i:])] or [[]]

########################################################

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) <= 1: return [[s]]
        
        cache = {0: [[s[0]]]}
        
        for i in range(1, len(s)):
            res = []
            if s[:i+1] == s[:i+1][::-1]:
                res.append([s[:i+1]])
            for j in range(i, 0, -1):
                # s[j:i+1] is palindrome
                val = s[j:i+1]
                if val != val[::-1]:
                    continue
                for prev in cache[j-1]:
                    res.append(prev + [val])
            cache[i] = res
                    
        return res