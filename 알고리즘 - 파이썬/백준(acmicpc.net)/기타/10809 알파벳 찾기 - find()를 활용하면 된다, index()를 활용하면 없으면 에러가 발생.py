string = input()

for i in range(26):
    print("%d" % string.find(chr(ord('a')+i)), end = " ")