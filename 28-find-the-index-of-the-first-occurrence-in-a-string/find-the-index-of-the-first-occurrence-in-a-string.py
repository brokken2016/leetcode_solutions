class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for x in range(len(haystack)):
            end = x + len(needle)
            
            if end <= len(haystack) and haystack[x: end] == needle:               
                return x
        return - 1

            