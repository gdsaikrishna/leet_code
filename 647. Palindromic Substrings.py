class Solution:
    def countSubstrings(self, S: str) -> int:
        ans, n, i = 0, len(S), 0
        while (i < n):
            j, k = i - 1, i
            while k < n - 1 and S[k] == S[k+1]: k += 1                
            ans += (k - j) * (k - j + 1) // 2
            i, k = k + 1, k + 1
            while ~j and k < n and S[k] == S[j]:
                j, k, ans = j - 1, k + 1, ans + 1
        return ans
    
    '''
    def expand(left: int, right: int) -> int:
		    count = 0
			while left >= 0 and right < len(s) and s[left] == s[right]:
			    # count the palindrome and expand outward
			    count += 1
				left -= 1
				right += 1
			return count
		
		palindromes = 0
		for i in range(len(s)):
		    # the idea is to expand around the 'center' of the string, but the center could be 1 or 2 letters
			# e.g., babab and cbbd, hence the (i, i) and (i, i + 1)
		    palindromes += expand(i, i)
			palindromes += expand(i, i+ 1)
		return palindromes
    '''