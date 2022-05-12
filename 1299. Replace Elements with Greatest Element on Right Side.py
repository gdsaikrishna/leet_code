class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        prev, post = -1, -1
        for i in range(len(arr)-1,-1,-1):
            prev = post
            post = max(post, arr[i])
            arr[i] = prev
        return arr