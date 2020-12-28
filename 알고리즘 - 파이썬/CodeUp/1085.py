h, b, c, s = map(int, input().split())

print("%.1f" % ((h*b*c*s)/(8*1024*1024)) + " MB")

# print('%.1f' % (44100*16*2*10/(8 * 1024 * 1024)))