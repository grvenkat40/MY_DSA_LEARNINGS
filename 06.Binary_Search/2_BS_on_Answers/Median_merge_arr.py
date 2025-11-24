class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        arr=[]
        m=len(nums1)
        n=len(nums2)
        i=0
        j=0
        while i<m and j<n:      
            if nums1[i]<=nums2[j]:
                arr.append(nums1[i])
                i+=1
            elif nums1[i]>nums2[j]:
                arr.append(nums2[j])
                j+=1
        while i<m:      
            arr.append(nums1[i])
            i+=1
        while j<n:      
            arr.append(nums2[j])
            j+=1
        # print(arr)
        if len(arr)%2==1:
            return arr[len(arr)//2]
        else:
            return ((arr[len(arr)//2])+(arr[len(arr)//2-1]))/2
        
obj=Solution()
# nums1 = [1,3]
# nums2 = [2]
nums1 = [1,2]
nums2 = [3,4]
print(obj.findMedianSortedArrays(nums1,nums2))