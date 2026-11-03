class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency = {}
        res = []

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        meow = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
        
        for x in range(k):
            res.append(meow[x][0])
            
        return res

