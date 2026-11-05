class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        s = set(nums)
        res = 0

        for num in s:
            if num - 1 in s:
                continue

            for j in range(len(s)):
                num += 1

                if not num in s:
                    
                    if res < j + 1:
                        res = j + 1 
                    break
        return res