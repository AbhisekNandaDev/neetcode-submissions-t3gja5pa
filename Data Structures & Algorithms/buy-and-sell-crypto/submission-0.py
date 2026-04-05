class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)  # track cheapest buy day
            profit = price - min_price        # best profit if selling today
            max_profit = max(max_profit, profit)
        return max_profit