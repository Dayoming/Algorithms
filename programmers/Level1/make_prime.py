def solution(nums):
    # Initialize count, sum_nums
    count = 0
    sum_nums = []

    # Pick three numbers and add them
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                sum_nums.append(nums[i] + nums[j] + nums[k])

    # Determine prime number
    for i in sum_nums:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime == True:
            count += 1
    return count


print(solution([1, 2, 7, 6, 4]))
