import sys
# input = sys.stdin.readline

tree = {}
cnt = 0
while True:
    x = input().rstrip()
    
    if not x:
        break
    
    if x in tree:
        tree[x] += 1
    else:
        tree[x] = 1
    
    cnt += 1

tree_list = list(tree.items())
tree_list.sort()

for tree in tree_list:
    print("%s %.4f" % (tree[0], tree[1]/cnt*100))
    