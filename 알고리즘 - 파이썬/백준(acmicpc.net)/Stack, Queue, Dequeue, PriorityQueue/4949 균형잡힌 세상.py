import sys
# input = sys.stdin.readline

def dfs(string):
    global flag
    st = []
    for ch in string:
        if ch == '(' or ch == '[':
            st.append(ch)
        elif ch == ')':
            if len(st) == 0 or st.pop() != '(':
                flag = False
                return 
        elif ch == ']':
            if len(st) == 0 or st.pop() != '[':
                flag = False
                return
    if len(st) != 0:
        flag = False

while True:
    flag = True
    string = input().rstrip()
    if string == '.':
        break
    else:
        dfs(string)
        if flag == False:
            print("no")
        else:
            print("yes")
