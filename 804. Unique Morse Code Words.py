class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---",".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        res = set()
        for word in words:
            m = []                           
            for ch in word:
                m.append(codes[ord(ch) - 97])
            res.add("".join(m))
        return len(res)