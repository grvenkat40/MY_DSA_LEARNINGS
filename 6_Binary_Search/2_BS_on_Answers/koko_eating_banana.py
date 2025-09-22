import math
class Solution:
    def minEatingSpeed(self, piles ,h) -> int:
        i=1
        j=max(piles)
        ans=-1
        while i<=j:
            mid=(i+j)//2
            if self.findBanana(piles,mid) <=h:
                ans=mid
                j=mid-1
            else:
                i=mid+1
        return ans
    def findBanana(self,piles,hour):
        total_time=0
        for banana in piles:
            total_time+=math.ceil(banana/hour)
        return total_time



piles = [3,6,7,11]        #4
h = 8
# piles = [30,11,23,4,20]     #30
# h = 5
# piles = [30,11,23,4,20]     #23
# h = 6
obj=Solution()
print(obj.minEatingSpeed(piles,h))