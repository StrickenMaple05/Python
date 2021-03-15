import time

def likes(names):
    length = len(names)
    if length == 0: output = "no one likes this"
    elif length == 1: output = "%s likes this" % names[0]
    elif length == 2: output = "%s and %s like this" % (names[0], names[1])
    elif length == 3: output = "%s, %s and %s like this" % (names[0], names[1], names[2])
    else: output = "%s, %s and %d others like this" % (names[0], names[1], length - 2)
    return output


def likes1(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)


names = ['Alex', 'Jacob', 'Mark', 'Max']
start_time = time.time()
print(likes(names))
print(time.time() - start_time)
start_time = time.time()
print(likes1(names))
print(time.time() - start_time)
