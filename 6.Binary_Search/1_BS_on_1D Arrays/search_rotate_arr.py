class Solution:
    def search(self, nums, target) -> int:
        i=0
        j=len(nums)-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid] == target:
                return mid
            if nums[i] <= nums[mid]:
                if nums[i] <= target and target < nums[mid]:
                    j=mid-1
                else:
                    i=mid+1
            else:
                if nums[mid] <= target and target <= nums[j]:
                    i=mid+1
                else:
                    j=mid-1
        return -1

obj=Solution()
# nums = [4,5,6,7,0,1,2]
# target = 0
nums = [4,5,6,7,0,1,2]
target = 3
print(obj.search(nums,target))