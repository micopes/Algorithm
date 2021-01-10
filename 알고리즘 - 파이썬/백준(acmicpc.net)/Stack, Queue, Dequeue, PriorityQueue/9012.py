n = int(input())

for i in range(n):
    st = []
    string = input()
    flag = True
    for j in range(len(string)):
        if string[j] == '(':
            st.append('(')
        elif string[j] == ')':
            if len(st) == 0:
                print("NO")
                flag = False
                break
            else:
                st.pop()
    if len(st) != 0:
        print("NO")
    elif flag == True:
        print("YES")