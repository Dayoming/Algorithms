def solution(a, b):
    # Save the days of the week to an array
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    # Save the month to an array
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Add all the dates from January to that day
    days = sum(month[:a - 1]) + b - 1
    # Find the day of the week by dividing by 7
    answer = week[days % 7]
    return answer
