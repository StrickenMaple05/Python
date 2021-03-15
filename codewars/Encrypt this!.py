def encrypt_this(text):
    words = text.split()
    string = []
    for word in words:
        if len(word) == 1:
            string.append(str(ord(word)))
        else:
            edited = list(word)
            edited[1], edited[len(edited) - 1] =\
                edited[len(edited) - 1], edited[1]
            edited[0] = str(ord(edited[0]))
            string.append(''.join(edited))
    return ' '.join(string)


print(encrypt_this("A wise old owl lived in an oak"))