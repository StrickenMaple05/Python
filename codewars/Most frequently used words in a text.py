from collections import Counter
import re


def top_3_words(text):
    if len(text) == 0:
        return {}
    s = re.sub(r'[_.,!?/:;\-]+', ' ', text)
    words = {}
    for word in re.findall(r'[\S+."]+', s):
        lower_word = word.lower()
        if not re.match("[']?[a-z]", lower_word):
            continue
        words[lower_word] = words.get(lower_word, 0) + 1
    sorted_words = list({k: v for k, v in sorted(words.items(), key=lambda item: item[1], reverse=True)}.keys())
    answer = []
    answer_size = min(3, len(words))
    for i in range(answer_size):
        answer.append(sorted_words[i])
    return answer


# OMFG, how can they create such an optimized solution
def top_3_words2(text):
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    return [w for w,_ in c.most_common(3)]


print(top_3_words2("'pnaajx 'pnaajx 'pnaajx 'pnaajx 'pnaajx e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))
