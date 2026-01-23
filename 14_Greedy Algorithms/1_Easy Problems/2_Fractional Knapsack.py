class Solution:
    def fractionalKnapsack(self, val, wt, cap):
        items = []
        for i in range(len(val)):
            items.append((val[i]/wt[i], val[i], wt[i]))
        remaining = cap
        total = 0.0
        for ratio, value, weight in items:
            if remaining == 0:
                break
            if weight <= remaining:
                total += value
                remaining -= weight
            else:
                total += ratio * remaining
                remaining = 0
        return total 

obj = Solution()
val = [60,100,120]
wt = [10,20,30]
cap = 50
print(obj.fractionalKnapsack(val, wt, cap))