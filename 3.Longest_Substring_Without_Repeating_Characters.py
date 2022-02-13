class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        start , maxlen= 0, 0
        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] >= start:
                start = dic[s[i]] + 1
            dic[s[i]] = i
            maxlen = max(maxlen, i-start+1)
        return maxlen