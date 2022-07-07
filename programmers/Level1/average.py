def solution(arr):
    sum_num = 0  # Variable to store the added value
    for i in arr:
        sum_num += i  # Sum arr value
    return sum_num / len(arr)  # added value / arr length
