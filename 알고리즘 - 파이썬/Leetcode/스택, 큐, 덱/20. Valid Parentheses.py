class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)
            else:
                if ch == ')':
                    if len(stack) > 0 and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                if ch == '}':
                    if len(stack) > 0 and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                if ch == ']':
                    if len(stack) > 0 and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False
                
