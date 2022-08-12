def solution(s):
    result = s
    number_str = {0: 'zero', 1: 'one', 2: 'two', 3: 'three',
                  4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    for i in number_str:
        if number_str[i] in s:
            result = result.replace(number_str[i], str(i))
    return int(result)


print(solution("one4seveneight"))
