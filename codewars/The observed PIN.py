adjacent = {
    '1': ['1', '2', '4'],
    '2': ['1', '2', '3', '5'],
    '3': ['2', '3', '6'],
    '4': ['1', '4', '5', '7'],
    '5': ['2', '4', '5', '6', '8'],
    '6': ['3', '5', '6', '9'],
    '7': ['4', '7', '8'],
    '8': ['5', '7', '8', '9', '0'],
    '9': ['6', '8', '9'],
    '0': ['8', '0']
}


def get_pin(observed):
    if len(observed) == 1:
        return observed[0]
    length = len(observed[0])
    sub_pin = get_pin(observed[1:])
    answer = [v for _ in range(length) for v in sub_pin]
    size = len(sub_pin)
    for i in range(length):
        for j in range(size * i, size * (i + 1)):
            answer[j] = observed[0][i] + answer[j]
    return answer


def get_pins(observed):
    array = list(observed)
    for i in range(len(array)):
        array[i] = adjacent.get(array[i])
    return get_pin(array)


print(get_pins('369'))