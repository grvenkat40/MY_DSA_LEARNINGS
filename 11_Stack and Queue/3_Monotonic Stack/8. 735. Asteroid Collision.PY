class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                if stack[-1] < -a:
                    stack.pop()
                    continue
                elif stack[-1] == -a:
                    stack.pop()
                break
            else:
                stack.append(a)
        return stack

obj = Solution()
# asteroids = [3,5,-6,2,-1,4]
asteroids = [10,2,-5]
print(obj.asteroidCollision(asteroids))