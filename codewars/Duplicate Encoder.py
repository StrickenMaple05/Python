def duplicate_encode(word):
    chars = {}
    lower_word = word.lower()
    for c in list(lower_word):
        chars[c] = chars.get(c, 0) + 1
    answer = ""
    for c in list(lower_word):
        answer += "(" if chars[c] == 1 else ")"
    return answer


# another one god solution
def duplicate_encode1(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])


print(duplicate_encode("din"))
