class OrderedStream:

    def __init__(self, n: int):
        self.S = [None]*(n+1)
        self.i = 1
        
    def insert(self, id: int, value: str) -> List[str]:
        self.S[id] = value
        while self.i < len(self.S):
            if not self.S[self.i]:
                break
            self.i += 1
        return self.S[id:self.i]
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)