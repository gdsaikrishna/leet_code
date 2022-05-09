class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        completed = set()
        for index, char in enumerate(s):
            if char in dic:
                if dic[char] != t[index]:
                    return False
            else:
                if t[index] in completed:
                    return False
                dic[char] = t[index]
                completed.add(t[index])
        return True