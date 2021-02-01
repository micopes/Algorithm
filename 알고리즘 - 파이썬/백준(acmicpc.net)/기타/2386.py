import sys
# input = sys.stdin.readline

while True:
    string = input()
    if string[0] == '#':
        break
    string = string.lower()
    cnt = 0
    char = string[0]
    for i in range(2, len(string)):
        if string[i] == char:
            cnt += 1
    print("%c %d" %(char, cnt))
