"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # queue의 시작 순서로 정렬을 해서 일자 리스트에 존재하는 (start, end) 쌍 end가 최대인 것뒤에 추가한다.
        #   - end가 최대인 것보다 start가 크다면 하나를 append한다.
        # 우선순위큐로 하고 싶지만 그냥 정렬로 처리. - 시간복잡도 여유있어서.

        # [반례]
        # 요소가 0개인 경우
        if len(intervals) == 0:
            return 0

        intervals.sort(key = lambda x : x.start)
        schedules = []
        schedules.append([(intervals[0].start, intervals[0].end)])
        for i in range(1, len(intervals)):
            schedules.sort(key = lambda x : x[-1][1])
            # 모든 end보다 start 시간이 앞선다면, 스케줄을 추가해야 함.
            # =[(0,40),(5,10),(15,20)]
            print(schedules)
            if schedules[0][-1][1] > intervals[i].start:
                schedules.append([(intervals[i].start, intervals[i].end)])
            else:
                for j in range(len(schedules)-1, -1, -1):
                    # 가장 end가 늦은 스케줄에 붙이는게 이득이므로. - 붙이면 넘긴다.
                    if schedules[j][-1][1] <= intervals[i].start:
                        schedules[j].append((intervals[i].start, intervals[i].end))
                        break

        print(schedules)
        return len(schedules)
