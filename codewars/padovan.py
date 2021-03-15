import time


def padovan(n):
    length = min(15, n) + 1
    padovans = [0] * length
    i = 0
    while i < length:
        padovans[i] = 1 if i < 3 else padovans[i - 2] + padovans[i - 3]
        i += 1

    if n <= 15:
        return padovans[n]

    mod = n % 5
    div = n / 5
    if mod == 0:
        i = mod + 4
        div -= 1
    else:
        i = mod - 1

    while i <= 14:
        div -= 1
        i += 5
    minus_fourteenth = padovans[i - 14]
    minus_ninth = padovans[i - 9]
    minus_fifth = padovans[i - 5]
    minus_fourth = padovans[i - 4]

    while div >= 0:
        current_elem = 4 * minus_fifth + minus_fourteenth
        next_elem = current_elem + minus_fourth

        minus_fourteenth, minus_ninth, minus_fifth, minus_fourth = \
            minus_ninth, minus_fourth, current_elem, next_elem
        div -= 1

    answer = minus_fourth
    return answer


def padovan2(n):
    # length = min(n, 15 + (n / 5 - 3) * 2)
    padovans = [0 for i in range(16)]
    for i in range(len(padovans)):
        if i < 3:
            padovans[i] = 1
        else:
            padovans[i] = padovans[i - 2] + padovans[i - 3]
    if n < 15:
        return padovans[n]

    large_padovans = []
    mod = n % 5
    div = n / 5
    if mod == 0:
        i = mod + 4
        div -= 1
    else:
        i = mod - 1

    while i <= 14:
        div -= 1
        i += 5

    array = [padovans[i - 14], padovans[i - 9], padovans[i - 5], padovans[i - 4]]
    k = 4

    while i <= n - 1:
        array.append(4 * array[k - 2] + array[k - 4])
        array.append(array[k] + array[k - 1])
        k += 2
        # padovans[i] = 4 * padovans[i - 5] + padovans[i - 14]
        # padovans[i + 1] = padovans[i] + padovans[i - 4]
        i += 5

    return array[len(array) - 1]


start_time = time.time()
print(padovan(1000000))
print("\n--- %s seconds ---" % (time.time() - start_time))

# $0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 $15 $16
