class Solution:
    def lemonadeChange(self, bills) -> bool:
        five = 0
        ten = 0
        for n in bills:
            if n == 5:
                five += 1
            elif n == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:
                if five >=1 and ten >= 1:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True      

obj = Solution()
bills = [5,5,5,10,20]
print(obj.lemonadeChange(bills))