class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start_index = 0
        
        if sum(gas) < sum(cost):
            return -1
        
        cur = 0
        # unique answer
        for i in range(len(gas)):
            cur = cur + gas[i] - cost[i]
            if cur < 0:
                start_index = i+1
                cur = 0
        
        return start_index
    
