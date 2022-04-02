class Solution:
    def validPalindrome(self, s: str) -> bool:
        h, t = 0, len(s) - 1
        while h < t:
            if s[h] != s[t]:
                 return s[h:t] == s[h:t][::-1] or s[h + 1:t + 1] == s[h + 1:t + 1][::-1]
            h, t = h + 1, t - 1
        return True