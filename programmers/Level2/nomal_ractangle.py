import math


def solution(w, h):  # Find the maximum common divisor
    return w * h - (w + h - math.gcd(w, h))
