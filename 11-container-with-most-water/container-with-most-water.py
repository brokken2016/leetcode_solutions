class Solution:
    def maxArea(self, height: list[int]) -> int:
        if height[0] > height[len(height) - 1]:
            lowest = height[len(height) - 1]
        else:
            lowest = height[0]

        res = (len(height) - 1) * lowest
        l, r = 0, len(height) - 1
        while r > l:
            
            if height[l] > height[r]:
                lowest = height[r]
            else:
                lowest = height[l] 
                
            if (r - l) * lowest > res:
                res = (r - l) * lowest

            if height[l] > height[r]:
                r -= 1
            elif height[l] < height[r]:
                l += 1
            else:
                r -= 1
                l += 1
        return res