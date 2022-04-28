class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = list(address)
        res = []
        for i in address:
            if i == ".":
                res += ["["+"."+"]"]
            else:
                res.append(i)
        return "".join(res)