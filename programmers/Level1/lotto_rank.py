def solution(lottos, win_nums):
    max_rank_value = 0
    min_rank_value = 0
    rank_list = [6, 6, 5, 4, 3, 2, 1]

    for i in lottos:
        if i in win_nums:
            min_rank_value += 1
            max_rank_value += 1
        if i == 0:
            max_rank_value += 1

    for i in range(0, len(rank_list)):
        max_rank = rank_list[max_rank_value]
        min_rank = rank_list[min_rank_value]
    answer = [max_rank, min_rank]
    return answer


solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
