class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i, price_i in enumerate(prices):
            for j, price_j in enumerate(prices[i:]):
                profit = price_j - price_i
                if profit > max_profit:
                    max_profit = profit
        
        return max_profit
