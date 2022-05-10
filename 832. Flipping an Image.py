class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[0 if x==1 else 1 for x in x][::-1] for x in image] 