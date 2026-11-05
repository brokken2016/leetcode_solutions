class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while r > l:
            if not s[r].isalpha() and not s[r].isdigit():
                r -= 1
                continue

            if not s[l].isalpha() and not s[l].isdigit():
                l += 1
                continue

            if s[r].lower() != s[l].lower():
                return False

            r -= 1
            l += 1
        return True
        