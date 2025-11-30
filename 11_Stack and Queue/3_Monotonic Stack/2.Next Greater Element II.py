class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        nge = [0]*n
        stack = []
        for i in range(2*n-1, -1, -1):
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
            if i < n:
                if not stack:
                    nge[i] = -1
                else:
                    nge[i] = stack[-1]
            stack.append(nums[i%n])
        return nge
    
obj = Solution()
nums = [1,2,3,4,3]
print(obj.nextGreaterElements(nums))