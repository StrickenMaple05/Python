def encode_rail_fence_cipher(string, n):
    answer = ""
    max_step = (n - 1) * 2
    for start in range(n):
        i = start
        step = (n - start - 1) * 2
        step = step if step != 0 else max_step
        while i < len(string):
            answer += string[i]
            i += step
            step = max_step - step if max_step != step else step
    return answer


def decode_rail_fence_cipher(string, n):
    answer = ["" for _ in range(len(string))]
    max_step = (n - 1) * 2
    length = len(string)
    i = 0
    for start in range(n):
        k = start
        step = (n - start - 1) * 2
        step = step if step != 0 else max_step
        while k < length:
            answer[k] = string[i]
            k += step
            i += 1
            step = max_step - step if max_step != step else step
    return "".join(answer)


print(encode_rail_fence_cipher("Hello, World!", 4))
print(decode_rail_fence_cipher("H !e,Wdloollr", 4))
