class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            else:
                # 스택이 비어있는 경우
                if len(stack) == 0:
                    return False
                pair_c = stack.pop()
                
                if c == ')':
                    if pair_c != '(':
                        return False
                elif c == '}':
                    if pair_c != '{':
                        return False
                elif c == ']':
                    if pair_c != '[':
                        return False
        
        # 스택에 남아 있으면 쌍이 안맞는 것
        if len(stack) > 0:
            return False
        else:
            return True
