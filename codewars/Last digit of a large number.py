cycle = {
    0: [0],
    1: [1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1]
}


def last_digit(n1, n2):
    if n2 == 0:
        return 1
    if n1 == 0:
        return 0
    last_digit = n1 % 10
    last_digit_cycle = cycle.get(last_digit)
    length = len(last_digit_cycle)
    return last_digit_cycle[(n2 - 1) % length]


print(last_digit(2, 8))
