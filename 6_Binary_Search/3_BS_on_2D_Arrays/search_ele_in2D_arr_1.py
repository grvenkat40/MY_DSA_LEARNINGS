class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        for row in range(len(matrix)):
            is_found=self.find_target(matrix[row],target)
            if is_found==True:
                return True
        else:
            return False
    def find_target(self,nums,target):
        i=0
        j=len(nums)-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid]==target:
                return True
            elif nums[mid]<target:
                i=mid+1
            else:
                j=mid-1

obj=Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(obj.searchMatrix(matrix,target))