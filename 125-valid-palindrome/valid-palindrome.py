class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for x in s:
            if x.isalpha() or x.isdigit():
                res += x.lower()
        l, r = 0, len(res) - 1

        while r > l:
            if res[r] != res[l]:
                return False
            r -= 1
            l += 1
        return True
        