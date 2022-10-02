# 풀이
# 1. 투포인터
# 2. reverse()를 사용
```
class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
        
        return s
```
