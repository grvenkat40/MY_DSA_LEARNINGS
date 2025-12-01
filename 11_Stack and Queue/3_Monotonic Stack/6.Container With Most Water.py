class Solution:
    def maxArea(self, height) -> int:
        total = 0
        left = 0
        right = len(height) -1
        while left < right:
            if height[left] <= height[right]:
                t1 = min(height[left], height[right]) * (right-left)
                left += 1
            elif height[left] > height[right]:
                t1 = min(height[left], height[right]) * (right-left)
                right -= 1
            total = max(t1, total)
        return total
    
obj = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(obj.maxArea(height))