class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        new_price = []
        stack = []
        for i in range(len(prices)-1, -1, -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()
            discount = stack[-1] if stack else 0
            pay = prices[i] - discount

            stack.append(prices[i])
            new_price.append(pay)
        return new_price[::-1]

obj = Solution()
prices = [8,4,6,2,3]
print(obj.finalPrices(prices))