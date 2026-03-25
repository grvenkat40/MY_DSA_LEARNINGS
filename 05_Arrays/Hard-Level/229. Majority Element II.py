class Solution:
    def MYSolution_majorityElement(self, nums: list[int]) -> list[int]:
        hash = {}
        need = len(nums)/3
        res = []                            #Time :- O(n)
        for n in nums:                      # Space :- O(n)
            hash[n] = hash.get(n, 0)+1
            if hash[n] > need:
                if n not in res:
                    res.append(n)
        return res
    
    # At most 2 elements can appear more than n/3 times

    def Optimal_majorityElement(self, nums: list[int]) -> list[int]:
        # Boyer-Moore Voting Algorithm
        if not nums:
            return []
        c1 = c2 = None
        v1 = v2 = 0
        for n in nums:
            if c1 == n:
                v1 += 1
            elif c2 == n:
                v2 += n
            elif v1 == 0:
                c1 = n
            elif v2 == 0:
                c2 = n
            else:
                v1 -= 1
                v2 -= 1
        # Verify
        res = []
        for c in [c1, c2]:
            if c and nums.count(c) > len(nums)//3:
                res.append(c)
        return res

obj = Solution()
nums = [3, 2, 3]
print("My solution", obj.MYSolution_majorityElement(nums))
print("Optimal solution", obj.Optimal_majorityElement(nums))