dp = [0 for _ in range(5001)] # 0 ~ 4999자리. <= 1 ~ 5000

def calc(string):
    global dp
    if string[0] == '0':
        dp[0] = 0
    else:
        dp[0] = 1
        
    for i in range(1, len(string)+1):
        x = int(string[i-1])
        if x >= 1 and x <= 9:
            dp[i] += dp[i-1]
            dp[i] %= 1000000
        if i == 1:
            continue
        y = int(string[i-2:i])
        if y >= 10 and y <= 26 :
            dp[i] += dp[i-2]
            dp[i] %= 1000000
    
    
    
# main
string = input()
calc(string)
print(dp[len(string)])

