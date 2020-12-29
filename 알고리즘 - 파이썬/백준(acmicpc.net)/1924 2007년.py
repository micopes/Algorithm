day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
m, d = map(int, input().split())

result = 0
for i in range(m-1):
    result += day[i]
result += d
    
result %= 7
print(week[result])

