from itertools import combinations

def solution(m, weights):
    answer = 0
    for cnt in range(1, len(weights)):
        totals = map(sum, combinations(weights, cnt))
        for total in totals:
            if total == m:
                answer += 1         
    return answer
