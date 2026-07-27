class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy_prices = prices[0]

        for i in range (len(prices)):
            profit = prices[i] - min_buy_prices
            if prices[i] < min_buy_prices:
                min_buy_prices = prices[i]
            if profit > max_profit:
                max_profit = profit
        return max_profit
