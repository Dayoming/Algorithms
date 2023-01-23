# 유클리드 호제법을 사용해서 최대공약수를 구한다
def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

# 두 수를 곱한 값을 최대공약수로 나눈다
def lcm(a, b):
    result = (a * b) // gcd(a, b)
    return result

a, b = map(int, input().split())

print(gcd(a, b))
print(lcm(a, b))