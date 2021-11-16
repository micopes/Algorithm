def mergeSort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    
    merged = []
    l = r = 0
    
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1
    
    # left, right 둘 중 하나는 다 merged에 채워진 상태. 나머지 한쪽을 merged에 append.
    while l < len(left):
        merged.append(left[l])
        l += 1
    while r < len(right):
        merged.append(right[r])
        r += 1
        
    return merged

arr = [6, 2, 41, 7, 752, 415, 57275, 1436, 14, 136, 11, 0]
print(mergeSort(arr))
    