import sys
# input = sys.stdin.readline

n = int(input().rstrip())
pw = input().rstrip()

length = n # 6글자 이상
num = 0 # 1개 이상
loAlp = 0 # 1개 이상
upAlp = 0 # 1개 이상
spe = 0 # 1개 이상
 
for i in range(len(pw)):
    if '0' <= pw[i] <= '9':
        num += 1
    elif 'a' <= pw[i] <= 'z':
        loAlp += 1
    elif 'A' <= pw[i] <= 'Z':
        upAlp += 1
    elif pw[i] in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']:
        spe += 1

if num == 0:
    length += 1
if loAlp == 0:
    length += 1
if upAlp == 0:
    length += 1
if spe == 0:
    length += 1

if length < 6:
    length += 6-length
    

result = length - n 
print(result)
    