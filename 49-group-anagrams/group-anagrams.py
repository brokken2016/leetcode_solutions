class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = []
        words = {}

        for word in strs:
            word_hash = {}
            for letter in word:
                word_hash[letter] = word_hash.get(letter, 0) + 1
            key = tuple(sorted(word_hash.items()))
            if key in words:
                words[key].append(word)
            else:
                words[key] = [word]
        for key in words:
            res.append(words[key])
                

        return res