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

mod_dict = {
    0: [0, 0],
    1: [1, 1],
    2: [2, 0],
    3: [3, 1]
}


def last_digit_of_two(n1, n2):
    if n2 == 0:
        return 1
    if n1 == 0:
        return 0
    last = n1 % 10
    last_digit_cycle = cycle.get(last)
    length = len(last_digit_cycle)
    return last_digit_cycle[(n2 - 1) % length]


def last_digit1(lst):
    length = len(lst)
    if length == 0:
        return 1
    if length == 1:
        return lst[0] % 10
    power = [0, 1]
    for i in range(length - 1, 0, -1):
        number = lst[i]
        if number == 0:
            if power == [0, 0]:
                lst[i] = 1
                power = [0, 1]
            else:
                power = [0, 0]
        elif power == [0, 0]:
            lst[i] = 1
            power = [0, 1]
        else:
            a = [number // 4, number % 4]
            if a[1] == 0:
                lst[i] = 4
            elif a[1] == 1:
                lst[i] = 1
            elif a[1] == 2:
                if power[0] == 0 and power[1] == 1:
                    lst[i] = 2
                else:
                    lst[i] = 4
            elif a[1] == 3:
                lst[i] = mod_dict.get(3)[(power[1] + 1) % 2]
            power = a

    if lst[0] == 0 and power[0] * 4 + power[1] == 0:
        return 1
    return last_digit_of_two(lst[0], lst[1])


# im out
def last_digit(lst):
    n = 1
    for x in reversed(lst):
        n = x ** (n if n < 4 else n % 4 + 4)
    return n % 10


print(last_digit([]))
print(last_digit([0, 0]))
print(last_digit([0, 0, 0]))
print(last_digit([1, 2]))
print(last_digit([3, 4, 5]))
print(last_digit([4, 3, 6]))
print(last_digit([7, 6, 21]))
print(last_digit([12, 30, 21]))
print(last_digit([2, 2, 2, 0]))
print(last_digit([937640, 767456, 981242]))
print(last_digit([123232, 694022, 140249]))
print(last_digit([499942, 898102, 846073]))