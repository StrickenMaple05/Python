step = {
    'n': [0, 1],
    's': [0, -1],
    'e': [1, 0],
    'w': [- 1, 0]
}


def is_valid_walk(walk):
    is_valid = True
    if len(walk) != 10:
        is_valid = False
    else:
        coordinate = [0, 0]
        for cur_step in walk:
            direction = step.get(cur_step)
            coordinate[0] += direction[0]
            coordinate[1] += direction[1]
        if coordinate != [0, 0]:
            is_valid = False

    return is_valid


print(is_valid_walk(['n', 'n', 'n', 'n', 'n', 's', 's', 's', 's', 's']))
