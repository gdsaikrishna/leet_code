class Solution:
    def maximum69Number (self, num: int) -> int:
        try: return int(str(num).replace('6','9',1))
        except: return num
        
'''
Solution without changing datatype
        i = 1000
        while i > 0:
            if num / i % 9 != 0:
                return num + 3 * i
            i /= 10
        return num
'''