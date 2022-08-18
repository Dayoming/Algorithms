def solution(s):
    answer = True
    mystack = []

    # Accessing indexes and elements of s
    for idx, bracket in enumerate(s):
        if bracket == "(":
            mystack.append(bracket)
        else:
            try:
                if mystack.pop() == "(":
                    pass
            except:
                answer = False
                break
    if len(mystack):
        answer = False

    return answer
