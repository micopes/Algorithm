import sys
# input = sys.stdin.readline

def right_bracket(string):
    stack = []
    for x in string:
        if x == '(' or x == '[':
            stack.append(x)
        elif x == ']':
            if len(stack) == 0:
                return False
            k = stack.pop()
            if k != '[':
                return False
        elif x == ')':
            if len(stack) == 0:
                return False
            k = stack.pop()
            if k != '(':
                return False
    
    if len(stack) == 0:
        return True
    else:
        return False
def solve(string):
    stack = []
    for x in string:
        if x == '(' or x == '[':
            stack.append(x)
        elif x == ')':
            temp = 2
            while stack:
                k = stack.pop()
                if type(k) == int:
                    temp *= k
                elif k == '(':
                    stack.append(temp)
                    break
        elif x == ']':
            temp = 3
            while stack:
                k = stack.pop()
                if type(k) == int:
                    temp *= k
                elif k == '[':
                    stack.append(temp)
                    break
        # 2개인 경우 더해서 저장
        temp = 0
        while stack:
            k = stack.pop()
            if type(k) == int:
                temp += k
            else:
                stack.append(k)
                break
        if temp:
            stack.append(temp)
    
    return stack[-1]

string = input().rstrip()
stack = []

if right_bracket(string):
    print(solve(string))
else:
    print(0)
