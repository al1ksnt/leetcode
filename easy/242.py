class Solution:
    def calc_letters(self, word: str) -> list[int]:
        res = [0] * (ord('z') - ord('a') + 1)   
        for letter in word:
            res[ord(letter) - ord('a')] += 1
        return res

    def isAnagram(self, s: str, t: str) -> bool:
        return len(s) == len(t) \
            and self.calc_letters(s) == self.calc_letters(t)
