word = input()

for i in range(len(word)):
    print('[%c' % (word[i]), end = '')
    for j in range(4 - i) :
        print('0', end = '')
    print(']')