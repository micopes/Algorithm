# isdigit() : 텍스트의 모든 문자가 숫자인지 확인 - string에 '0' ~ '9'인 것을 판별
# 16행에 x.split()[1:] 와 같이 이후 index를 모두 포함시켜서 lambda function을 이용할 수 있다.

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
                    
        letters.sort(key = lambda x : (x.split()[1:], x.split()[0]))
        return letters + digits
        