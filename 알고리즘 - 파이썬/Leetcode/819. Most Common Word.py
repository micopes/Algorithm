# 정규표현식
# dic.items()

import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = []
        dic = {}
        for word in re.sub(r'[^\w]', ' ', paragraph).lower().split():
            if word not in banned:
                if word not in dic:
                    dic[word] = 1
                else:
                    dic[word] += 1
                
        word_nums = list(dic.items())
        word_nums.sort(key = lambda x : x[1], reverse = True)
        return word_nums[0][0]
                
        
        