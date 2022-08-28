class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        
        for cur_index, cur_value in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < cur_value:
                idx = stack.pop()
                res[idx] = cur_index - idx
            stack.append(cur_index)
            
        return res
            
                
