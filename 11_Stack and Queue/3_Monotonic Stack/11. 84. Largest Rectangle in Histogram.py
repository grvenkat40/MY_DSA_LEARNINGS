class BruteSolution:
    def largestRectangleArea(self, heights) -> int:
        n = len(heights)
        def get_prev_smaller(heights):
            stack = []
            pse = [0]*n
            for i in range(n):
                while stack and heights[stack[-1]] > heights[i]:
                    stack.pop()
                if stack:
                    pse[i] = stack[-1]
                else:
                    pse[i] = -1
                stack.append(i)
            print(pse)
            return pse
        def get_next_smaller(heights):
            stack = []
            nse = [0]*n
            for i in range(n-1, -1, -1):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if stack:
                    nse[i] = stack[-1]
                else:
                    nse[i] = n
                stack.append(i)
            print(nse)
            return nse
        
        area = 0
        prev = get_prev_smaller(heights)
        nxt = get_next_smaller(heights)
        for i in range(n):
            width = nxt[i] - prev[i] -1
            area = max(area, (heights[i]*width))
        return area

"""----------------------------------------------------------------------------------------"""

class OptimalSolution:
    def largestRectangleArea(self, heights) -> int:
        n = len(heights)
        def get_prev_smaller(heights):
            stack = []
            pse = [0]*n
            for i in range(n):
                while stack and heights[stack[-1]] > heights[i]:
                    stack.pop()
                if stack:
                    pse[i] = stack[-1]
                else:
                    pse[i] = -1
                stack.append(i)
            return pse
        def get_next_smaller(heights):
            stack = []
            nse = [0]*n
            for i in range(n-1, -1, -1):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if stack:
                    nse[i] = stack[-1]
                else:
                    nse[i] = n
                stack.append(i)
            return nse
        
        area = 0
        prev = get_prev_smaller(heights)
        nxt = get_next_smaller(heights)
        for i in range(n):
            width = nxt[i] - prev[i] -1
            area = max(area, (heights[i]*width))
        return area


obj = BruteSolution()
heights = [2,1,5,6,2,3]
print("Brute Solution")
print(obj.largestRectangleArea(heights))

obj1 = OptimalSolution()
heights = [2,1,5,6,2,3]
print("Optimal Solution")
print(obj1.largestRectangleArea(heights))
