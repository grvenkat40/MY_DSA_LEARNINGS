class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        hash = {}
        ans = []
        mini = float("inf")
        for i, word in enumerate(list1):
            hash[word] = i
        for i, word in enumerate(list2):
            if i > mini:
                break
            if word in hash:
                curr_sum = hash[word] + i
                if curr_sum == mini:
                    mini = curr_sum
                    ans.append(word)
                else:
                    if curr_sum < mini:
                        mini = curr_sum
                        ans = [word]
        return ans