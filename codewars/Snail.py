def snail(snail_map):
    if snail_map == [[]]:
        return []
    i = 0
    j = -1
    dir = 1
    counter = len(snail_map)
    answer = []
    while counter != 0:
        for k in range(counter):
            j += dir
            answer.append(snail_map[i][j])
        counter -= 1
        for k in range(counter):
            i += dir
            answer.append(snail_map[i][j])
        dir *= -1
    return answer


print(snail([[1,2,3],
         [4,5,6],
         [7,8,9]]))
