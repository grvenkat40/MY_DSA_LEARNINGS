class Solution:
    def MinimumCoins(self, coins, amount):
        summ = sum(coins)
        if summ <= amount:
            return amount-summ
        else:
            return -1
    
obj = Solution()
coins = [1, 2, 5]
amount = 11
print(obj.MinimumCoins(coins, amount))