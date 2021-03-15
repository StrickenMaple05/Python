def smaller(arr):
    array = []
    n = len(arr)
    for i in range(n):
        amount = 0
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                amount += 1
        array.append(amount)
    return array


print(smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]))
