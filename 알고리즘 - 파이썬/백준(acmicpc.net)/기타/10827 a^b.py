import sys
from decimal import Decimal, getcontext
# input = sys.stdin.readline

# str에서 Decimal로 변환해야 한다.
# float에서 Decimal로 변환하면 float 자료형의 부정확성때문에 이상한 값 나옴.

a, b = input().rstrip().split()
# 최대 99.999999999 => 11자리 * 99 -> 1100 자릿수
getcontext().prec = 1101
print("{0:f}".format(Decimal(a)**int(b)))