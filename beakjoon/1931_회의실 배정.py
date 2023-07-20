import sys

def maximum_meetings(n, meetings):
    # 회의 종료 시간, 시작 시간을 기준으로 정렬
    # 종료 시간 기준으로 정렬하면 3 3, 2 3의 회의가 들어왔을 때 2 3을 진행할 수 없다고 판단하게 됨
    sorted_meetings = sorted(meetings, key = lambda x : (x[1], x[0]))
    
    # 첫 번째 회의는 무조건 선택
    selected_meetings = [sorted_meetings[0]]
    last_end_time = sorted_meetings[0][1]
    
    for i in range(1, n):
        start_time, end_time = sorted_meetings[i]
        
        # 회의가 겹치지 않으면 선택
        if start_time >= last_end_time:
            selected_meetings.append((start_time, end_time))
            last_end_time = end_time

    return len(selected_meetings)

N = int(sys.stdin.readline())
meetings = []
    
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    meetings.append((start, end))
        
result = maximum_meetings(N, meetings)
print(result)
