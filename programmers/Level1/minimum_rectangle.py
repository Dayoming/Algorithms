def solution(sizes):
    # Save Widths
    width = []
    # Save Heights
    height = []
    # Repeat a two-dimensional list
    for i in sizes:
        # If width >= height
        if i[0] >= i[1]:
            width.append(i[0])
            height.append(i[1])
        # If height >= width
        else:
            width.append(i[1])
            height.append(i[0])
    return max(width) * max(height)


print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
