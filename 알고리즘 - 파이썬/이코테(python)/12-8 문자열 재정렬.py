import sys
# input = sys.stdin.readline

string = input()

string_list = []
sum_num = 0

for ch in string:
    if ch >= 'A' and ch <= 'Z':
        string_list.append(ch)
    else:
        sum_num += int(ch)

string_list.sort()

ans = "".join(string_list)
ans += str(sum_num)

print(ans)
        

