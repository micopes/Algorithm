from collections import deque
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        result.append(intervals[0])

        for i in range(1, len(intervals)):
            if result[-1][0] <= intervals[i][0] <= result[-1][1]:
                if result[-1][1] < intervals[i][1]:
                    temp = [result[-1][0], intervals[i][1]]
                    result.pop()
                    result.append(temp)
            else:
                result.append(intervals[i])

        return result
