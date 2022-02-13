class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0 : return 0
        chars = list(s)
        sign = -1 if chars[0] == '-' else 1
        if chars[0] == '-' or chars[0] == '+' : del chars[0]
        ans, i = 0, 0
        while i < len(chars) and chars[i].isdigit() :
            ans = ans*10 + ord(chars[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * ans,2**31-1))