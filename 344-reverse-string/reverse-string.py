class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while r > l:
            left_char = s[l]
            right_char = s[r]
            if right_char != left_char:
                s[r] = left_char
                s[l] = right_char
            r -= 1
            l += 1
            