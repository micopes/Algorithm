s = input()
s += '2'

num = [0, 0] # [0] : 0, [1] : 1

for i in range(1, len(s)):
    if s[i-1] == s[i]:
        continue
    else:
        num[int(s[i-1])] += 1
        
print(min(num))

