class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '')
        
        head = len(s) % k
        
        grouping = []
        if head:
            grouping.append( s[:head] )
        for index in range(head, len(s), k ):
            grouping.append( s[ index : index+k ] )
        return '-'.join( grouping ).upper()