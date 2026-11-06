class Solution:
    def trap(self, height: list[int]) -> int:
        result = 0

        first = 0
        while first < len(height) - 1 and height[first] <= height[first + 1]:
            first += 1

        last = len(height) - 1
        while last > 0 and height[last] <= height[last - 1]:
            last -= 1

        print(first, last)
        x = first + 1

        highest_i = 0
        highest_val = 0
        seen = []
        while x <= last:
            
            if height[x] > highest_val:              
                highest_i = x
                highest_val = height[x]    

            if highest_val >= height[first] or last == x:
                diff = 0

                for j in range(first + 1, highest_i):
                    diff += height[j]

                print(height[first], diff, highest_val)
                result += (min(height[first], highest_val) * (highest_i - first - 1)) - diff
                
                first = highest_i
                x = first + 1
                highest_i = x

                if x > last:
                    break
                highest_val = 0
                
                continue
        
            x += 1
                
        return result