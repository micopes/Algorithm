import sys
input = sys.stdin.readline

string = input().rstrip()
exp = input().rstrip()
exp_len = len(exp)

ans = []
for i in range(len(string)):    
    ans.append(string[i])
    check = False
    if string[i] == exp[-1] and len(ans) >= exp_len:
        check = True
        for j in range(exp_len):
            if ans[len(ans)-1 - j] != exp[exp_len-1 - j]:
                check = False
        
        if check == True:
            for k in range(exp_len):
                ans.pop()

if len(ans) != 0:
    ans = "".join(ans)
    print(ans)
else:
    print("FRULA")
    
    