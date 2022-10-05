from itertools import combinations
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return
            
            for i in range(index, len(digits)):
                for c in dic[digits[i]]:
                    dfs(i+1, path + c)
        
        dic = {'2': "abc",
               '3': "def",
               '4': "ghi",
               '5': "jkl",
               '6': "mno",
               '7': "pqrs",
               '8': "tuv",
               '9': "wxyz"}
        
        result = []
        if digits == "":
            return []
        dfs(0, "")
            
        return result
