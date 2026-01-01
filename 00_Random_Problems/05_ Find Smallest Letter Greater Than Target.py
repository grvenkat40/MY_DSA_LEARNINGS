class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        i = 0
        j = len(letters)-1
        ans = letters[0]
        while i <= j:
            mid = (i+j)//2
            if ord(letters[mid]) > ord(target):
                ans = letters[mid]
                j = mid-1
            else:
                i = mid+1
                
        return ans if ord(ans) > ord(target) else letters[0]
obj = Solution()
letters = ["c","f","j"]
target = "a"
print(obj.nextGreatestLetter(letters, target))