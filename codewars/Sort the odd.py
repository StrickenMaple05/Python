def sort_array(source_array):
    indexes = []
    odds = []
    for i in range(len(source_array)):
        if source_array[i] % 2 == 0:
            continue
        indexes.append(i)
        odds.append(source_array[i])
    odds = sorted(odds)
    for i in range(len(indexes)):
        source_array[indexes[i]] = odds[i]
    return source_array


def sort_array2(arr):
    odds = sorted((x for x in arr if x % 2 != 0), reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in arr]


print(sort_array2([5, 3, 2, 8, 1, 4]))
