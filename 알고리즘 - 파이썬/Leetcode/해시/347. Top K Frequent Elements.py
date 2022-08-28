class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for x in nums:
            if x in dic:
                dic[x] += 1
            else:
                dic[x] = 1

        temp = list(dic.items())
        temp.sort(key = lambda x : x[1], reverse = True)

        res = []
        for i in range(k):
            res.append(temp[i][0])

        return res
