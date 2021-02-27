n = int(input().rstrip())

r, M = 31, 1234567891

string = input().rstrip()
ans = 0
for i in range(n):
    a = ord(string[i]) - ord('a') + 1
    ans += a*pow(r, i)
    ans %= M

print(ans)