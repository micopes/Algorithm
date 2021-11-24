import sys
# input = sys.stdin.readline

def solve():
    P, K, H, T = 13, 13, 13, 13
    for i in range(0, n, 3):
        temp = string[i:i+3]
        if temp in is_dupli:
            print("GRESKA")
            return 
        is_dupli.add(temp)
        if temp[0] == 'P':
            P -= 1
        elif temp[0] == 'K':
            K -= 1
        elif temp[0] == 'H':
            H -= 1
        elif temp[0] == 'T':
            T -= 1
    
    print(P, K, H, T)
    return 
# 중복 여부가 나오면 바로 GRESKA를 리턴하는 것으로.
is_dupli = set()
string = input().rstrip()
n = len(string)

solve()
    
        

