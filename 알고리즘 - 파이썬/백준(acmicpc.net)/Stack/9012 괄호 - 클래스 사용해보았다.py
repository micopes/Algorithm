class Stack:
    def __init__(self):
        self.data = []
    def clear(self):
        self.data.clear()
    def push(self, item):
        self.data.append(item)
    def top(self):
        return self.data[-1]
    def isEmpty(self):
        return len(self.data) == 0
    def pop(self):
        return self.data.pop()
    
def checkBracket(string):
    stack = Stack()
    for ch in string:
        if ch in ('[', '{', '('):
            stack.push(ch)
        elif ch in (']', '}', ')'):
            if stack.isEmpty():
                return False
            else:
                left = stack.top()
                if (ch == ')' and left == '(') or\
                    (ch == '}' and left == '{') or\
                    (ch == ']' and left == '['):
                        stack.pop()
                else:
                    return False
    
    return stack.isEmpty()
                
            
            
    
n = int(input())

for i in range(n):
    string = input()
    if(checkBracket(string) == True):
        print("YES")
    else:
        print("NO")
    
    
    