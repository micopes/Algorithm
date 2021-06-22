def solution(prices):
    answer = [0 for _ in range(len(prices))]
    
    st = []
    
    for i in range(len(prices)):
        while st and prices[i] < prices[st[-1]]:
            j = st.pop()
            answer[j] = i - j
        st.append(i)
    
    while st:
        x = st.pop()
        answer[x] = len(prices) - 1 - x
    
    return answer