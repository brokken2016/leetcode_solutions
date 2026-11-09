class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest = prices[0]
        result = 0

        for x in prices:
            if x - lowest > result:
                result = x - lowest
            if x < lowest:
                lowest = x

        return result