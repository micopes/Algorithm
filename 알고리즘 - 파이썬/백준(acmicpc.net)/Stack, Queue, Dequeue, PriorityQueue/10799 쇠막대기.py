st = []
string = input()
result = 0

for i in range(len(string)):
    if string[i] == '(':
        if string[i+1] == ')':
            continue;
        else:
            st.append(1)
    elif string[i] == ')':
        if string[i-1] == '(': # 레이저
            for j in range(len(st)):
                st[j] += 1
        else: # 레이저 아니고 그냥 하나 닫힌거
            if len(st) != 0:
                result += st.pop()

print(result)