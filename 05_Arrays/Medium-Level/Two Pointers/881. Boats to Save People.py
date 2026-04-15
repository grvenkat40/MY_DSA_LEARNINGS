class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        boat = 0
        people.sort()
        i = 0
        j = len(people)-1
        while i <= j:
            total = people[i] + people[j]
            if total > limit:
                j -= 1
                boat += 1
            elif total <= limit:
                i += 1
                boat += 1
                j -= 1
        return boat
obj = Solution()
print(obj.numRescueBoats(people = [3,2,2,1], limit = 3))