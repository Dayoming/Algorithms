# Hashing
import sys

l = int(sys.stdin.readline())
table = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8,
'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 
'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

s = sys.stdin.readline().strip()
hashing = 0

for i in range(len(s)):
    hashing += table[s[i]] * (31 ** i)

# 유한한 범위의 출력을 위해 큰 수로 나눈 나머지를 취한다(모듈러 연산)
print(hashing % 1234567891)