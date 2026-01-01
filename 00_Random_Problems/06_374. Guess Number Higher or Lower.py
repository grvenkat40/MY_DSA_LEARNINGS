# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

class Solution:
    def guess(self, num: int) -> int:
        pick = 6
        if num == pick:
            return 0
        elif num > pick:
            return -1
        else:
            return 1
        
    def guessNumber(self, n: int) -> int:
        i = 0
        j = n
        while i <= j:
            mid = (i+j)//2
            result = self.guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                j = mid
            else:
                i = mid + 1
        return -1

obj =Solution()
n = 10
pick = 6
print(obj.guessNumber(n))