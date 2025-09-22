class MY_Solution:
    def intersection(self, nums1, nums2):
        result=[]
        i=0
        j=0
        nums1.sort()
        nums2.sort()
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                if nums1[i] not in result:
                    result.append(nums1[i])
                i+=1
                j+=1
        return result
    

    def better(self,nums1,nums2):
        know=set(nums1)
        result=[]
        for i in nums2:
            if i in know:
                if i not in result:
                    result.append(i)
            
        return result

obj=MY_Solution()
# nums1=[9,4,9,8,4]
# nums2=[4,9,5]
nums1=[1,2,2,1]
nums2=[2,2]
print(obj.intersection(nums1,nums2))
print(obj.better(nums1,nums2))