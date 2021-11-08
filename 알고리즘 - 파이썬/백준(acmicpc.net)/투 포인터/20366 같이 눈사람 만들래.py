# 효율적인 다른 사람 코드
import sys
# input = sys.stdin.readline

n = int(input().rstrip())

snow = list(map(int, input().rstrip().split()))
snow.sort()

ans = sys.maxsize

for i in range(n-3):
    for j in range(i+3, n):
        val = snow[i] + snow[j]
        
        start = i+1
        end = j-1
        while start < end:
            temp = snow[start] + snow[end]
            ans = min(ans, abs(val - temp))
            
            if val > temp:
                start += 1
            elif val < temp:
                end -= 1
            else:
                break
            
print(ans)
                    
            
'''
# 내 코드
import sys
input = sys.stdin.readline

n = int(input().rstrip())

snow = list(map(int, input().rstrip().split()))
snow.sort()

ans = sys.maxsize

for i in range(n):
    for j in range(i+1, n):
        val = snow[i] + snow[j]
        # 사이에 2개 없으면 다음으로 넘어가기
        if j-i-1 < 2:
            continue
        
        for k in range(i+1, j):
            start = i+1
            end = j-1
            # index : k 는 포함안되도록
            while start <= end:
                mid = (start + end) // 2
                temp = snow[k] + snow[mid]
                
                if val < temp:
                    if k != mid:
                        ans = min(ans, abs(val - temp))
                    end = mid - 1
                    
                else:
                    if k != mid:
                        ans = min(ans, abs(val - temp))
                    start = mid + 1

print(ans)
                    
'''