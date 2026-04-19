class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        l1 = len(nums1)
        l2 = len(nums2)
        i = 0
        j = 0
        res = 0
        while i < l1 and j < l2:
            if nums1[i] <= nums2[j]:
                res = max(res, (j-i))
                j += 1
            else:
                i += 1
        return res

obj = Solution()
print(obj.maxDistance(nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]))