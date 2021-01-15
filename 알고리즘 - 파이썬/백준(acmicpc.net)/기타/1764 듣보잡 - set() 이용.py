n, m = map(int, input().split())

a = set()
b = set()

for i in range(n):
    string = input()
    a.add(string)
for i in range(m):
    string = input()
    b.add(string)
    
result = list(a&b)
result.sort()
print(len(result))
for val in result:
    print(val)