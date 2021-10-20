import sys
input = sys.stdin.readline

dictionary = {}

n = int(input().rstrip())

li = []

for i in range(n):
    name, record = input().rstrip().split()
    if record == 'enter':
        dictionary[name] = 1
    else:
        dictionary[name] = 0

for key, item in dictionary.items():
    if item == 1:
        li.append(key)

li.sort(reverse = True)
for name in li:
    print(name)
