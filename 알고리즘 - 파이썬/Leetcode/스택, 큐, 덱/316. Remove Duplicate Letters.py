class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = collections.Counter(s)
        
        visited, stack = set(), []
    
        for ch in s:
            count[ch] -= 1
            if ch not in visited:
                while len(stack) > 0 and stack[-1] > ch and count[stack[-1]] > 0:
                    visited.remove(stack.pop())
                stack.append(ch)
                visited.add(ch)
                        
        return "".join(stack)
