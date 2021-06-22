# 트럭 순서는 바꿀 수 없다.(원 문제 참고)
def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_bridge = [0]*bridge_length # 여기가 핵심!
    
    while on_bridge:
        answer += 1
        on_bridge.pop(0)
        if truck_weights:
            if sum(on_bridge) + truck_weights[0] <= weight:
                on_bridge.append(truck_weights[0])
                truck_weights.pop(0)
            else:
                on_bridge.append(0)
    
    return answer
        
    
    
    