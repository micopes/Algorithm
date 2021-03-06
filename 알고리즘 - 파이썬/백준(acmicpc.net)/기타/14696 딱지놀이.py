import sys
# input = sys.stdin.readline

def solve(a, b):
    if a[4] > b[4]:
        print("A")
        return
    elif a[4] < b[4]:
        print("B")
        return
    if a[3] > b[3]:
        print("A")
        return
    elif a[3] < b[3]:
        print("B")
        return
    if a[2] > b[2]:
        print("A")
        return
    elif a[2] < b[2]:
        print("B")
        return
    if a[1] > b[1]:
        print("A")
        return
    elif a[1] < b[1]:
        print("B")
        return
    
    print("D")
    return

t = int(input().rstrip())

for _ in range(t):
    a = [0, 0, 0, 0, 0]
    b = [0, 0, 0, 0, 0]
    listA = list(map(int, input().rstrip().split()))
    for i in range(1, len(listA)):
        a[listA[i]] += 1
    listB = list(map(int, input().rstrip().split()))
    for i in range(1, len(listB)):
        b[listB[i]] += 1
    
    solve(a, b)