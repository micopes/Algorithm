class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
            
        temp = []
        for key in dic.keys():
            temp.append((key, dic[key]))
        
        temp.sort(key = lambda x : -x[1])
        
        result = []
        for i in range(k):
            result.append(temp[i][0])
        
        return result
            
                
            
