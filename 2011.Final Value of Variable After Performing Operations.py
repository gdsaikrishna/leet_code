class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for operation in operations:
            ans = ans + 1 if operation in ["++X","X++"] else ans-1
        return ans