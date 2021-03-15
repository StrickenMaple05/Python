import re


def decipher_this(string):

    words = string.split()
    pattern = "([0-9]+)([a-zA-Z]+)"
    new_string = []
    for word in words:
        split = re.search(pattern, word)
        if split:
            first = split.group(1)
            second = list(split.group(2))
            second[0], second[len(second) - 1] =\
                second[len(second) - 1], second[0]
            new_word = chr(int(first)) + ''.join(second)
            new_string.append(new_word)
        else:
            new_string.append(chr(int(word)))
    return " ".join(new_string)


print(decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"))
