import re


def to_camel_case(text):
    if len(text) == 0:
        return ""
    char = text[0]
    answer = ""
    for word in re.split('-|_', text):
        answer += word.capitalize()
    answer = char + answer[1:]
    return answer


def to_camel_case_optimized(text):
    return text[0] + text.title().translate(None, "-_")[1:] if text else text


print(to_camel_case_optimized("Hello-i_am-artem"))

