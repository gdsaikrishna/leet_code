class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pointer = len(digits)-1
        while digits[pointer] == 9:
            digits[pointer] = 0
            pointer -= 1
        if pointer < 0:
            return [1]+digits
        else:
            digits[pointer] += 1
            return digits