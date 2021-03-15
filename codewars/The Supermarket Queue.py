import time


def queue_time(customers, n):
    tills = [0] * n
    m = len(customers)
    current = 0
    time = -1
    process = True
    while process:
        process = False
        time += 1
        for i in range(n):
            if tills[i] == 0:
                if current == m:
                    continue
                tills[i] = customers[current] - 1
                process = True
                current += 1
            else:
                process = True
                tills[i] -= 1
    return time


def queue_time2(customers, n):
    l = [0] * n
    for i in customers:
        l[l.index(min(l))] += i
    return max(l)


start_time = time.time()
print(queue_time([1, 2, 3, 4, 5], 10000000))
print(time.time() - start_time)
start_time = time.time()
print(queue_time2([1, 2, 3, 4, 5], 10000000))
print(time.time() - start_time)
