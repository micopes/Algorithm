class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 모든 티켓은 한번만 사용해야 하고, 한번은 사용해야 한다.
        graph = collections.defaultdict(list)
        
        for a, b in sorted(tickets):
            graph[a].append(b)
        
        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())
        
        return route[::-1]
