class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock = {}
        for it, val in enumerate(prices):
            stock[it] = val
            
        max1 = 0

        for it, val in enumerate(prices):
            tmp = max((stock[x] for x in stock if x > it), default=0) - val
            if tmp > max1:
                max1 = tmp
        return max1

        