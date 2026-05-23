class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = {}
        for s in strs:
            v = self.vectorize(s)
            res.setdefault(v, [])
            res[v].append(s)
        return list(res.values())

    def vectorize(self, word: str) -> tuple[int, ...]:
        res = [0] * (ord('z') - ord('a') + 1)   
        for letter in word:
            res[ord(letter) - ord('a')] += 1
        return tuple(res)
