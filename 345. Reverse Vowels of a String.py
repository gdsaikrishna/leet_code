class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels, s = set('aeiouAEIOU'), list(s)
        left, right = 0, len(s)-1
        
        while left <= right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
            elif s[right] not in vowels:
                right -= 1
                continue
            elif s[left] not in vowels:
                left += 1
                continue
            left += 1
            right -= 1
        
        return ''.join(s)