class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        a = [s for s in range(len(S)+1)]
        return [a.pop(0) if i == "I" else a.pop(-1)  for i in S] + a