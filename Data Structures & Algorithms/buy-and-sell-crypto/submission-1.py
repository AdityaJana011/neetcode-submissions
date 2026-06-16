class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for p in prices[1:]:
            #update the best buy so far
            if p < min_price:
                min_price = p
            else:
                #update the best profit with selling today
                max_profit = max(max_profit, p - min_price)

        return max_profit