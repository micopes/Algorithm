# 방법
# 1. 스택 이용
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        result = 0
        
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                top = stack.pop()
                
                if len(stack) == 0:
                    break
                
                x = i - stack[-1] - 1
                y = min(height[stack[-1]], height[i]) - height[top]
                
                result += x * y
            
            stack.append(i)
                
        return result
