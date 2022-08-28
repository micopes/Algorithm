class Solution:
    def smallestSubsequence(self, s: str) -> str:
        count = collections.Counter(s) # 남은 것
        
        visited = set() # stack에 존재
        stack = []
        
        for ch in s:
            count[ch] -= 1
            if ch not in visited: 
                while stack and stack[-1] > ch and count[stack[-1]] > 0:
                    visited.remove(stack.pop())
                visited.add(ch) # 스택에 없다면 어쩔 수 없이 넣어야 함.(위의 while문으로 최적의 위치 만들기.)
                stack.append(ch)
        
        return "".join(stack)
        
        
        
            
