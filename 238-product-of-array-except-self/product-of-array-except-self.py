class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = []
        mult = 1
        for i in range(len(nums)):
            
            if i > 0:
                mult = mult * nums[i - 1]
            res.append(mult)

        mult = 1
        for i in range(len(nums) -1, -1, -1):

            if i < len(nums) - 1:
                mult = mult * nums[i + 1]
            res[i] = res[i] * mult

        return res


             