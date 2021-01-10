string = input()

result = [0 for _ in range(26)]

for i in range(len(string)):
    result[ord(string[i])-ord('a')] += 1

for i in range(len(result)):
    print("%d" % result[i], end = " ")
    
    