from itertools import product


def solution(word):
    answer = 0
    dictionary = []
    for i in range(1, 6):
        dictionary.extend(
            list(map(''.join, product(['A', 'E', 'I', 'O', 'U'], repeat=i))))
        dictionary.sort()
        return dictionary.index(word) + 1
