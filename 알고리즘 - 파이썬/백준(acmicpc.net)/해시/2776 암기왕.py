# 두 풀이 모두 시간은 비슷하게 걸린다. set()을 이용한 풀이가 더 간단한 듯.

# 1. 집합(set())을 이용한 풀이
'''
import sys
# input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    
    n = int(input().rstrip())
    note = list(map(int, input().rstrip().split()))
    # note_dict = {}
    note_set = set()
    for x in note:
        note_set.add(x)
    
    m = int(input().rstrip())
    note2 = list(map(int, input().rstrip().split()))
    for x in note2:
        if x in note_set:
            print(1)
        else:
            print(0)
'''
# 2. 딕셔너리를 이용한 풀이

import sys
# input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    
    n = int(input().rstrip())
    note = list(map(int, input().rstrip().split()))
    note_dict = {}
    for x in note:
        note_dict[x] = 1
    
    m = int(input().rstrip())
    note2 = list(map(int, input().rstrip().split()))
    for x in note2:
        try:
            note_dict[x]
            print(1)
        except:
            print(0)
            