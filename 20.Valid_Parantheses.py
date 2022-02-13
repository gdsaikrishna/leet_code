class Solution:
    def isValid(self, s: str) -> bool:
        lis = []
        dic = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        for char in s:
            if char in dic:
                lis.append(char)
            else:
                if len(lis) == 0 or dic[lis[-1]] != char:
                    return False
                else:
                    lis.pop()
        return len(lis) == 0