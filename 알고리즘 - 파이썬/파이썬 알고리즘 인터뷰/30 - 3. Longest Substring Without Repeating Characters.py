from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        result = 0
        dq = deque()
        for c in s:
            if c in dic and dic[c] == 1:
                while dq:
                    x = dq.popleft()
                    dic[x] -= 1
                    if x == c:
                        break
            dic[c] = 1
            dq.append(c)
            
                
            result = max(result, len(dq))
            print(dq)
        return result
        

# 최적화
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_length = 0
        used = {}
        
        for idx, ch in enumerate(s):
            if ch in used and start <= used[ch]:
                start = used[ch] + 1
            else:
                max_length = max(max_length, idx - start + 1)
                
            used[ch] = idx
        return max_length
                
                
        
        
                
            
