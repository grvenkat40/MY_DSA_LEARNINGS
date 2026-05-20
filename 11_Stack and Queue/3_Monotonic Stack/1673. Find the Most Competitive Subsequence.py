class Solution:
    def mostCompetitive(self, nums,k):
        stack = []
        remove = len(nums) - k
        for i in range(len(nums)):
            while stack and stack[-1] > nums[i] and remove > 0:
                    stack.pop()
                    remove -= 1
            stack.append(nums[i])
        return stack[:k]

obj = Solution()
print(obj.mostCompetitive(nums = [2,4,3,3,5,4,9,6], k = 4))