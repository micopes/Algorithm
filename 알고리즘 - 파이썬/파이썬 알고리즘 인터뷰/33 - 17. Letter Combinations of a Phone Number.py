class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def dfs(index, string):
            # 종료 조건
            if len(string) == len(digits):
                result.append(string)
                return 
            
            
            for c in dic[digits[index]]:
                dfs(index+1, string+c)
        
        result = []
        if len(digits) == 0:
            return []
    
        dic = {'2': "abc",
               '3': "def",
               '4': "ghi",
               '5': "jkl",
               '6': "mno",
               '7': "pqrs",
               '8': "tuv",
               '9': "wxyz"}
        
        dfs(0, "") # idx, string
        return result
