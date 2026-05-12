class Solution:
    def MY_Solution_GREEDY_maximumJumps(self, nums: list[int], target: int) -> int:
        jump = 0
        left = 0
        right = 1
        while right < len(nums):
            if -target <= (nums[right] - nums[left]) <= target:
                jump += 1
                left = right
            right += 1
        return jump if (left == len(nums)-1) else -1

    def Optimal_DP_maximumJumps(self, nums: list[int], target: int) -> int:
        jump = [-1] * len(nums)
        jump[0] = 0
        for i in range(1, len(nums)):
            for j in range(i):
                if abs(nums[j] - nums[i]) <= target and jump[j] != -1:
                    jump[i] = max(jump[i], jump[j]+1)
        return jump[-1]
    
obj = Solution()
print(obj.MY_Solution_GREEDY_maximumJumps(nums = [1,3,6,4,1,2], target = 2))
print(obj.Optimal_DP_maximumJumps(nums = [1,3,6,4,1,2], target = 2))