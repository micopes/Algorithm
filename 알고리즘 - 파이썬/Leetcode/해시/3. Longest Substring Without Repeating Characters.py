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
