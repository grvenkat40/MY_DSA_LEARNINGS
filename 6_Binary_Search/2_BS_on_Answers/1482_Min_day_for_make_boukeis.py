class Solution:
    def minDays(self, bloomDay, boukaie, flower) -> int:
        i=min(bloomDay)
        j=max(bloomDay)
        ans=-1
        while i<=j:
            mid=(i+j)//2
            if self.findDay(bloomDay,mid,boukaie,flower) == True:
                ans=mid
                j=mid-1
            else:
                i=mid+1
        return ans
    def findDay(self,bloomDay,mid,boukaie,flower):
        boukaies=0
        cnt=0
        for day in bloomDay:
            if mid>=day:
                cnt+=1
            else:
                boukaies+=(cnt//flower)
                cnt=0
        boukaies+=(cnt//flower)
        if boukaie<=boukaies:
            return True
        else:
            return False
        
obj=Solution()
# bloomDay = [1,10,3,10,2]      #3
# boukaie = 3
# flower = 1
# bloomDay = [1,10,3,10,2]      #-1
# boukaie = 3
# flower = 2
bloomDay = [7,7,7,7,12,7,7]     #12
boukaie = 2
flower = 3

print(obj.minDays(bloomDay, boukaie, flower))