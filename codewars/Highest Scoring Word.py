def high(x):
    highest_score = 0
    highest_word = ""
    for word in x.split(' '):
        score = 0
        for c in list(word):
            score += ord(c) - 96
        if score <= highest_score:
            continue
        highest_word = word
        highest_score = score
    return highest_word


def high2(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


print(high2('what time are we climbing up the volcano'))
