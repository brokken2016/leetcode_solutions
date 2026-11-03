class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = []
        words = {}

        for word in strs:
            key = tuple(sorted(word))
            
            if key in words:
                words[key].append(word)
            else:
                words[key] = [word]

        for key in words:
            res.append(words[key])
                

        return res