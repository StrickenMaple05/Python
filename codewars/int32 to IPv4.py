import re


def int32_to_ip(int32):
    code = str(bin(int32)[2:])
    s = "0" * (32 - len(code)) + code
    ip = []
    for i in re.findall('[01]{8}', s):
        ip.append(str(int(i, 2)))
    return ".".join(ip)


print(int32_to_ip(32))
