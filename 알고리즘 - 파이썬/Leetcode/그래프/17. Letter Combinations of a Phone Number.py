from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, string):
            if len(string) == len(digits):
                result.append(string)
                return 
            
            for i in range(index, len(digits)):
                for x in dic[digits[i]]:
                    dfs(i+1, string+x)
        
        if not digits:
            return []
        
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
       "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        dfs(0, "")
        
        return result
        
        



