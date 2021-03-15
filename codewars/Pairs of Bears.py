import re


def bears(x, s):
    pairs = re.findall('B8|8B', s)
    return ["".join(pairs), len(pairs) * 2 >= x]


print(bears(8, 'cBkB8BBB8cB888BB8'))
