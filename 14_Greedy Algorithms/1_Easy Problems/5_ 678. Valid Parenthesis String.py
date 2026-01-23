class BruteSolution:
    def checkValidString(self, s: str) -> bool:
        cnt = 0
        ind = 0
        return self.check(s, ind, cnt)

    def check(self, s, ind, cnt):
        if cnt < 0:
            return False
        if ind == len(s):
            return cnt == 0
        if s[ind] == "(":
            return self.check(s, ind+1, cnt+1)
        if s[ind] == ")":
            return self.check(s, ind+1, cnt-1)
        return self.check(s, ind+1, cnt+1) or self.check(s, ind+1, cnt-1) or self.check(s, ind+1, cnt)

class OptimalSolution:
    def checkValidString(self, s: str) -> bool:
        min = 0
        max = 0
        for i in range(len(s)):
            if s[i] == "(":
                min += 1
                max += 1
            elif s[i] == ")":
                min -= 1
                max -= 1
            else:
                min -= 1
                max += 1
            if min < 0:
                min = 0
            if max < 0 :
                return False
        return min == 0

obj = BruteSolution()
s = "(*)"
print(obj.checkValidString(s))

obj = OptimalSolution()
s = "(*)"
print(obj.checkValidString(s))