class BruteSolution:
    def subArrayRanges(self, nums) ->int:
        total = 0
        subarr = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                subarr.append(nums[i:j+1])
        for arr in subarr:
            total += (max(arr) - min(arr))
        return total
    
"""-----------------------------------------------------------------------"""

class OptimalSolution:
    def subArrayRanges(self, nums) -> int:
        n = len(nums)

        def get_prev_smaller(nums):
            stack = []
            pse = [0]*n
            for i in range(n):
                while stack and nums[stack[-1]] > nums[i]:
                    stack.pop()
                if stack:
                    pse[i] = stack[-1]
                else:
                    pse[i] = -1
                stack.append(i)
            return pse
        def get_next_smaller(nums):
            stack = []
            nse = [0]*n
            for i in range(n-1, -1, -1):
                while stack and nums[stack[-1]] >= nums[i]:
                    stack.pop()
                if stack:
                    nse[i] = stack[-1]
                else:
                    nse[i] = n
                stack.append(i)
            return nse
        def get_prev_greater(nums):
            stack = []
            pge = [0]*n 
            for i in range(n):
                while stack and nums[stack[-1]] < nums[i]:
                    stack.pop()
                if stack:
                    pge[i] = stack[-1]
                else:
                    pge[i] = -1
                stack.append(i)
            return pge
        def get_next_greater(nums):
            stack = []
            nge = [0]*n
            for i in range(n-1, -1, -1):
                while stack and nums[stack[-1]] <= nums[i]:
                    stack.pop()
                if stack:
                    nge[i] = stack[-1]
                else:
                    nge[i] = n
                stack.append(i)
            return nge
        
        ps = get_prev_smaller(nums)
        ns = get_next_smaller(nums)
        pg = get_prev_greater(nums)
        ng = get_next_greater(nums)

        total = 0
        for i in range(n):
            max_cnt = (i- pg[i]) * (ng[i] - i)
            min_cnt = (i-ps[i]) * (ns[i] - i)
            total += (nums[i] * (max_cnt - min_cnt))
        return total
    
obj = BruteSolution()
# nums = [1,2,3]
nums = [4,-2,-3,4,1]
print("Brute Approach")
print(obj.subArrayRanges(nums))

obj1 = OptimalSolution()
# nums = [1,2,3]
nums = [4,-2,-3,4,1]
print("Optimal Approach")
print(obj1.subArrayRanges(nums))