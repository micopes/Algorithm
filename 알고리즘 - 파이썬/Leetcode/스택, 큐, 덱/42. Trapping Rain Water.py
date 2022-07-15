class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        
        n = len(height)
        for i in range(n):
            while stack and height[stack[-1]] < height[i]:
                top = stack.pop()
                if len(stack) == 0:
                    break
                    
                x = i - stack[-1] - 1
                y = min(height[i], height[stack[-1]]) - height[top]
                
                res += x * y
            stack.append(i)
        
        return res
                