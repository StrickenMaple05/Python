def first_non_repeating_letter(string):
    answer = ''
    array = list(string.lower())
    for c in string:
        if array.count(c.lower()) == 1:
            return c
    return answer


print(first_non_repeating_letter('moonmen'))
