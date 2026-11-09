class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        result = 0
        for x in range(len(s)):
            preres = ""
            preres += s[x]
            for y in range(x + 1, len(s)):
                if s[y] in preres:
                    break
                preres += s[y]
            result = max(result, len(preres))
            
        return result