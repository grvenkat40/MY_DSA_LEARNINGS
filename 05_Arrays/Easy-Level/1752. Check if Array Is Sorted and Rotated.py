class Solution:
    def Brute(self, nums: list[int]) -> bool:
        n=len(nums)
        for i in range(n):
            check_list=[]
            for j in range(i,n):
                check_list.append(nums[j])
            for k in range(i):
                check_list.append(nums[k])
            check=True
            for num in range(n-1):
                if check_list[num]>check_list[num+1]:
                    check=False
                    # return False
                    break
            if check:
                return True
        return False

    def Better(self, nums: list[int]) -> bool:
        sor = sorted(nums)
        for i in range(len(nums)):
            arr = nums[i:] + nums[:i]
            if arr == sor:
                return True
        return False

    def Optimal(self, nums: list[int]) -> bool:
        drops = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i+1)%len(nums)]:
                drops += 1
            if drops > 1:
                return False
        return True

obj = Solution()
nums = [3, 4, 5, 1, 2]
print(obj.Brute(nums))
print(obj.Better(nums))
print(obj.Optimal(nums))
    


        