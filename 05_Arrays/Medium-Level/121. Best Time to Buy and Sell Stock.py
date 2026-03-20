class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            curr_profit = price - min_price
            if curr_profit > profit:
                profit = curr_profit
        return profit

obj = Solution()
prices = [7,1,5,3,6,4]
print(obj.maxProfit(prices))