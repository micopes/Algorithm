# import sys
# input = sys.stdin.readline

while True:
    try:
        string = input()
        
        result = [0 for _ in range(4)]
        
        for i in range(len(string)):
            num = ord(string[i])
            if num >= ord('a') and num <= ord('z'):
                result[0] += 1
            elif num >= ord('A') and num <= ord('Z'):
                result[1] += 1
            elif num >= ord('0') and num <= ord('9'):
                result[2] += 1
            elif num == ord(' '):
                result[3] += 1
        print("%d %d %d %d" % (result[0], result[1], result[2], result[3]))
    except EOFError:
        break