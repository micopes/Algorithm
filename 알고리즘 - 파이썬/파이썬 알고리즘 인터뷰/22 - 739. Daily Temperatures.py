class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        day = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            while len(stack) > 0 and stack[-1][1] < temperatures[i]:
                idx, val = stack.pop()
                day[idx] = i - idx
                
            stack.append((i, temperatures[i])) # idx, val
        
        return day
            
        
