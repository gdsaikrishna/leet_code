class Solution:
    def calPoints(self, ops: List[str]) -> int:
        p = []
        for i in ops:
            if i == 'C': 
                p.pop()
            elif i == 'D': p.append(2*p[-1])
            elif i == '+': p.append(p[-1]+p[-2])
            else: p.append(int(i))
        return sum(p)