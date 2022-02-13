class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        mapping = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}
        
        chars = []
        for c in digits:
            chars.append(mapping[c])
            
        ans = [""]
        for i in range(len(chars)):
            ans=[c+chars[i][j] for c in ans for j in range(len(chars[i]))]
            
        return ans