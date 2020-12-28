number1, number2 = input().split('-')
number1 = int(number1)
number2 = int(number2)

print("%06d%07d" % (number1, number2))
