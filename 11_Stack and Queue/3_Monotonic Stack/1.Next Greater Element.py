class Solution:
    def nextGreaterElement(self, nums1, nums2):
        hash = {}
        result = []
        for i in range(len(nums2)):
            hash[nums2[i]] = i
        for num in nums1:
            ind = hash[num]
            found = -1
            for  k in range(ind+1,len(nums2)):
                if num < nums2[k]:
                    found = nums2[k]
                    break
            result.append(found)
        return result 

obj = Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(obj.nextGreaterElement(nums1, nums2))
