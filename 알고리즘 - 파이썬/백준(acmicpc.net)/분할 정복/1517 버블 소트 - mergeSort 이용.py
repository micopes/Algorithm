import sys
input = sys.stdin.readline

def merge(arr):
    global result
    if len(arr) <= 1:
        return
    mid = len(arr) // 2
    
    L = arr[:mid]
    R = arr[mid:]
    merge(L)
    merge(R)
    
    i = j = k = 0
    
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            result += (len(L) - i)
        k += 1
    
    # L, R 둘 중 하나가 남으면 남은 것 채우기.
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
        
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

result = 0
n = int(input().strip())
arr = list(map(int, input().strip().split()))
merge(arr)
print(result)

