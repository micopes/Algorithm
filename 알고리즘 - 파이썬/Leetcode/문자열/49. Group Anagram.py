class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}
        for s in strs:
            key = "".join(sorted(s))
            
            if key in dic:
                dic[key].append(s)
            else:
                dic[key] = [s]
        
        res = []
        for l in list(dic.items()):
            res.append(l[1])
        
        return res
            