"""A leader in an array is an element whose value is strictly greater than all elements to its right in the given array. 
The rightmost element is always a leader. 
The elements in the leader array must appear in the order they appear in the nums array."""

# nums = [1, 2, 5, 3, 1, 2]
nums = [-3, 4, 5, 1, -30, -10]
# nums = [-3, 4, 5, 1, -4, -5]
n = len(nums)
leader = []
if not leader:
    leader.append(nums[n-1])
for i in range(n-2,-1,-1):
    if nums[i]>nums[i+1]:
        leader.append(nums[i])
leader.reverse()
print(leader)