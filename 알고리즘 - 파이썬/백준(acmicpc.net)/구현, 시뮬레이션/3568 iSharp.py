import sys
input = sys.stdin.readline
l = list(input().rstrip().split())

for i in range(1, len(l)):
    temp_list = list(l[i])
    if temp_list[-1] == ',' or temp_list[-1] == ';':
        temp_list.pop()
    
    result_list = list(l[0])
    while temp_list[-1] in ['&', '[', ']', '*']:
        if temp_list[-1] == ']':
            result_list.append(temp_list[-2])
            result_list.append(temp_list[-1])
            temp_list.pop()
            temp_list.pop()
        else:
            result_list.append(temp_list[-1])
            temp_list.pop()
            
    
    for x in result_list:
        print(x, end = "")
    print(" ", end = "")
    for x in temp_list:
        print(x, end = "")
    print(';')
