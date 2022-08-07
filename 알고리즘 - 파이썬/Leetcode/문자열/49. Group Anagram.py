class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        
        for string in strs:
            key = "".join(sorted(string))
        
            if key not in dic:
                dic[key] = [string]
            else:
                dic[key].append(string)
        
        return list(dic.values())
                
        