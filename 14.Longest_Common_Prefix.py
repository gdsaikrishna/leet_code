class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        for s in zip(*strs):
            if len(set(s)) != 1: break
            ans += s[0]
        return ans

############################################################################
#strs = ["flower","flow","flight"]
#l = list(zip(*strs))
#>>> l = [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
############################################################################
#min of list of strings returns minimum string when sorted
#max returns maximum of strings when sorted
############################################################################
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        m, M = min(strs), max(strs)
        for i, letter in enumerate(m):
            if letter != M[i]:  return m[:i]
        return m