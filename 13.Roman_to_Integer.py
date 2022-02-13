class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
        }
        ans, i =  0, 0
        while i < len(s):
            ans += roman[s[i]]
            if i+1 < len(s):
                if roman[s[i]] < roman[s[i+1]]:
                    ans += roman[s[i+1]] - 2*roman[s[i]]
                    i+=1
            i+=1    
        return ans